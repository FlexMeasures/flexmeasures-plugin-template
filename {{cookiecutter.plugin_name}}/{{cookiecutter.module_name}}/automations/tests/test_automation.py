from datetime import timedelta

from marshmallow import ValidationError
import pytest
from rq.job import Job

from flexmeasures.data.automations import get_automation_handler, get_automation_types
from flexmeasures.data.models.generic_assets import GenericAsset, GenericAssetType
from flexmeasures.data.models.time_series import Sensor, TimedBelief
from flexmeasures.data.models.user import Account
from flexmeasures.data.services.automations import (
    create_automation,
    resolve_automation_sensors,
    run_automation,
)
from flexmeasures.data.utils import save_to_db
from flexmeasures.utils.job_utils import work_on_rq
from flexmeasures.utils.time_utils import server_now
import timely_beliefs as tb

from .. import __automation_types__

AUTOMATION_TYPE = __automation_types__[0].type_id


@pytest.fixture
def site(fresh_db):
    """A site with an input and an output sensor, and a sensor on another organisation's site."""
    asset_type = GenericAssetType(name="site")
    site = GenericAsset(
        name="Site",
        generic_asset_type=asset_type,
        owner=Account(name="Site owner"),
    )
    other_site = GenericAsset(
        name="Other site",
        generic_asset_type=asset_type,
        owner=Account(name="Other site owner"),
    )
    sensors = {
        name: Sensor(
            name=name,
            generic_asset=asset,
            unit="kW",
            event_resolution=timedelta(minutes=15),
        )
        for name, asset in (
            ("input", site),
            ("output", site),
            ("elsewhere", other_site),
        )
    }
    fresh_db.session.add_all(sensors.values())
    fresh_db.session.commit()
    return site, sensors


def make_automation(site, config, parameters=None):
    automation, _ = create_automation(
        asset=site,
        name="Example automation",
        cronstr="*/15 * * * *",
        automation_type=AUTOMATION_TYPE,
        config=config,
        parameters=parameters or {},
    )
    return automation


def test_automation_type_is_registered(app):
    handler = get_automation_types()[AUTOMATION_TYPE]
    generator_class = handler.generator_class
    assert app.data_generators["ingestor"][generator_class.__name__] is generator_class


@pytest.mark.parametrize("field", ["config", "parameters"])
def test_unknown_fields_are_rejected(fresh_db, site, field):
    site, sensors = site
    payload = {"config": {"sensor": sensors["output"].id}, "parameters": {}}
    payload[field]["unknown-field"] = 1
    with pytest.raises(ValidationError):
        make_automation(site, **payload)


def test_declared_sensors(fresh_db, site):
    site, sensors = site
    automation = make_automation(
        site, {"sensor": sensors["output"].id, "input-sensor": sensors["input"].id}
    )
    assert resolve_automation_sensors(automation) == {
        "input_sensors": [sensors["input"]],
        "output_sensors": [sensors["output"]],
    }


def test_output_must_belong_to_the_automated_asset(fresh_db, site):
    site, sensors = site
    with pytest.raises(ValueError, match="must belong to asset"):
        make_automation(site, {"sensor": sensors["elsewhere"].id})


def test_a_run_records_the_computed_value(app, fresh_db, site):
    site, sensors = site
    input_sensor, output_sensor = sensors["input"], sensors["output"]
    now = server_now()
    automation = make_automation(
        site,
        {"sensor": output_sensor.id, "input-sensor": input_sensor.id},
        {"offset": 1.5, "factor": 2},
    )
    save_to_db(
        tb.BeliefsDataFrame(
            [
                tb.TimedBelief(
                    sensor=input_sensor,
                    source=automation.generator,
                    event_start=now - timedelta(hours=1),
                    belief_time=now,
                    event_value=10,
                )
            ]
        )
    )
    fresh_db.session.commit()

    result = run_automation(automation)
    job = Job.fetch(result["job_id"], connection=app.redis_connection)
    work_on_rq(app.queues[get_automation_handler(AUTOMATION_TYPE).queue], job=job)
    job.refresh()
    assert job.is_finished, job.exc_info

    beliefs = (
        fresh_db.session.query(TimedBelief).filter_by(sensor_id=output_sensor.id).all()
    )
    assert [belief.event_value for belief in beliefs] == [1.5 + 2 * 10]
    assert beliefs[0].source_id == automation.generator_id
