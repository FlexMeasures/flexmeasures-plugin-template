"""
An example data generator, which an automation runs on its schedule.

It records one value on the configured sensor for the current time slot:
the `offset` parameter, plus `factor` times the latest value of the input sensor, if one is configured.
Replace the computation with your own, e.g. fetching data from an external service.
"""

from __future__ import annotations

from marshmallow import RAISE, Schema, fields
import pandas as pd
import timely_beliefs as tb

from flexmeasures.data.models.data_sources import DataGenerator
from flexmeasures.data.schemas.sensors import SensorIdField
from flexmeasures.utils.time_utils import server_now


class ExampleConfigSchema(Schema):
    """What the generator computes.

    A different configuration creates a different data source,
    so results computed with different settings can be told apart.
    """

    class Meta:
        unknown = RAISE

    sensor = SensorIdField(required=True)
    input_sensor = SensorIdField(required=False, data_key="input-sensor")


class ExampleParametersSchema(Schema):
    """How each run computes; these are stored on the automation and passed to every run."""

    class Meta:
        unknown = RAISE

    offset = fields.Float(load_default=0.0)
    factor = fields.Float(load_default=1.0)


class {{ cookiecutter.module_name|replace('_', ' ')|title|replace(' ', '') }}Generator(DataGenerator):
    __data_generator_base__ = "ingestor"
    # Bump the version whenever you change what the generator computes.
    # Existing automations then refuse to run until they are recreated, so old and new results never share a data source.
    __version__ = "0.1"
    _config_schema = ExampleConfigSchema()
    _parameters_schema = ExampleParametersSchema()

    # FlexMeasures checks access to every sensor listed here, and rejects results for any output sensor not listed.
    @property
    def input_sensors(self):
        return self._resolve_sensors(self._config.get("input_sensor"))

    @property
    def output_sensors(self):
        return self._resolve_sensors(self._config["sensor"])

    def _compute(self, offset: float, factor: float) -> list[dict]:
        sensor = self._config["sensor"]
        value = offset
        input_sensor = self._config.get("input_sensor")
        if input_sensor is not None:
            latest = input_sensor.latest_state()
            if latest.empty:
                raise ValueError(f"Input sensor {input_sensor.id} has no data yet.")
            value += factor * float(latest["event_value"].iloc[-1])

        now = server_now()
        # Record the value for the time slot we are in, as the sensor's resolution defines it (in UTC).
        event_start = pd.Timestamp(now).tz_convert("UTC")
        if sensor.event_resolution:
            event_start = event_start.floor(sensor.event_resolution)
        beliefs = tb.BeliefsDataFrame(
            [
                tb.TimedBelief(
                    sensor=sensor,
                    source=self.data_source,
                    event_start=event_start,
                    belief_time=now,
                    event_value=value,
                )
            ]
        )
        return [{"sensor": sensor, "data": beliefs}]
