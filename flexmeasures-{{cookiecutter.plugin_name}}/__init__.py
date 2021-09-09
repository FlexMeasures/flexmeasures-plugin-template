import os
import sys

import click
from flask import Blueprint
from flask.cli import with_appcontext
from flexmeasures.data.transactional import task_with_status_report


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

__version__ = "0.1"

{{cookiecutter.plugin_name}}_bp = Blueprint("{{cookiecutter.plugin_name}}", __name__)


{{cookiecutter.plugin_name}}_bp.cli.help = "{{cookiecutter.plugin_name}} commands"


@zinfo_bp.cli.command("hello-world")
@click.option(
    "--name",
)
@with_appcontext
@task_with_status_report
def hello_world(name: str):
    print(f"Hello, {name}")
