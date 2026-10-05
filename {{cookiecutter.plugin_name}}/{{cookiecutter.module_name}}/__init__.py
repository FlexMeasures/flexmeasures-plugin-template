__version__ = "0.1"


"""
The __init__ for the {{cookiecutter.plugin_name}} FlexMeasures plugin.

FlexMeasures registers the BluePrint objects it finds in here.
"""
{%- if cookiecutter.minimal_flexmeasures_version %}

import warnings
from importlib_metadata import version as pkg_version
from packaging.version import Version

try:
    _fm_version = pkg_version("flexmeasures")
    if Version(_fm_version) < Version("{{cookiecutter.minimal_flexmeasures_version}}"):
        warnings.warn(
            f"{{cookiecutter.plugin_name}} requires FlexMeasures >= {{cookiecutter.minimal_flexmeasures_version}}, "
            f"but version {_fm_version} is installed."
        )
except Exception:
    pass
{%- endif %}
{%- if cookiecutter.api_blueprint | lower == 'y' or cookiecutter.ui_blueprint | lower == 'y' or cookiecutter.cli_blueprint | lower == 'y' %}

from flask import Blueprint

from .utils import ensure_bp_routes_are_loaded_fresh
{%- endif %}
{%- if cookiecutter.api_blueprint | lower == 'y' %}

# API
{{cookiecutter.module_name}}_api_bp: Blueprint = Blueprint(
    "{{cookiecutter.plugin_name}} API",
    __name__,
    url_prefix="/{{cookiecutter.plugin_slug}}/api",
)
ensure_bp_routes_are_loaded_fresh("api.somedata")
from .api import somedata  # noqa: E402,F401
{%- endif %}
{%- if cookiecutter.ui_blueprint | lower == 'y' %}

# UI
{{cookiecutter.module_name}}_ui_bp: Blueprint = Blueprint(
    "{{cookiecutter.plugin_name}} UI",
    __name__,
    template_folder="ui/templates",
    url_prefix="/{{cookiecutter.plugin_slug}}",
)
ensure_bp_routes_are_loaded_fresh("ui.views.dashboard")
from .ui.views import dashboard  # noqa: E402,F401
{%- endif %}
{%- if cookiecutter.cli_blueprint | lower == 'y' %}

# CLI
CLI_HELP = "{{cookiecutter.plugin_name}} CLI commands"
{{cookiecutter.module_name}}_cli_bp: Blueprint = Blueprint(
    "{{cookiecutter.plugin_name}} CLI",
    __name__,
    cli_group="{{cookiecutter.plugin_slug}}",
)
{{cookiecutter.module_name}}_cli_bp.cli.help = CLI_HELP
ensure_bp_routes_are_loaded_fresh("cli.commands")
from .cli import commands  # noqa: E402,F401
{%- endif %}
