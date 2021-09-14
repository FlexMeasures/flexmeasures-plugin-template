import os
import sys

import click
from flask import Blueprint


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

__version__ = "0.1"  # TODO: get version via scm_stuptools


# API
{{cookiecutter.module_name}}_api_bp: Blueprint = Blueprint(
    "{{cookiecutter.plugin_name}} API", __name__, url_prefix="/{{cookiecutter.plugin_slug}}/api"
)
from {{cookiecutter.module_name}}.api import somedata  # noqa: E402,F401

# UI
{{cookiecutter.module_name}}_ui_bp: Blueprint = Blueprint(
    "{{cookiecutter.plugin_name}} UI", __name__, template_folder="ui/templates", url_prefix="/{{cookiecutter.plugin_slug}}"
)
from {{cookiecutter.module_name}}.ui.views import dashboard  # noqa: E402,F401

# CLI
{{cookiecutter.module_name}}_cli_bp: Blueprint = Blueprint(
    "{{cookiecutter.plugin_name}}", __name__
)
{{cookiecutter.module_name}}_cli_bp.cli.help = "{{cookiecutter.plugin_name}} CLI commands"
from {{cookiecutter.module_name}}.cli import commands  # noqa: E402,F401


