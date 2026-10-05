import os

import pytest

from flexmeasures.app import create as create_flexmeasures_app

# Use these fixtures to rely on the FlexMeasures database.
# There might be others in flexmeasures/conftest you want to also re-use.
from flexmeasures.conftest import db, fresh_db  # noqa: F401


@pytest.fixture(scope="session")
def app():
    print("APP FIXTURE")

    # Load this plugin from its folder, wherever pytest runs from; the folder name becomes the plugin name.
    plugin_folder = os.path.dirname(os.path.abspath(__file__))
    test_app = create_flexmeasures_app(env="testing", plugins=[plugin_folder])

    # Establish an application context before running the tests.
    ctx = test_app.app_context()
    ctx.push()

    yield test_app

    ctx.pop()

    print("DONE WITH APP FIXTURE")
