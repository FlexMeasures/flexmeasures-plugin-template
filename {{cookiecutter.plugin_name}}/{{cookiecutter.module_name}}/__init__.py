__version__ = "Unknown version"


"""
The __init__ for the {{cookiecutter.plugin_name}} FlexMeasures plugin.

FlexMeasures registers the BluePrint objects it finds in here.
"""


from importlib_metadata import version, PackageNotFoundError

from flask import Blueprint

from .utils import ensure_bp_routes_are_loaded_fresh

# Overwriting version (if possible) from the package metadata
# ― if this plugin has been installed as a package.
# This uses importlib.metadata behaviour added in Python 3.8.
# Note that we rely on git tags (via setuptools_scm) to define that version.
try:
    __version__ = version("{{cookiecutter.module_name}}")
except PackageNotFoundError:
    # package is not installed
    pass

{%- if cookiecutter.api_blueprint | lower == 'y' %}

# API
{{cookiecutter.module_name}}_api_bp: Blueprint = Blueprint(
    "{{cookiecutter.plugin_name}} API", __name__, url_prefix="/{{cookiecutter.plugin_slug}}/api"
)
ensure_bp_routes_are_loaded_fresh("api.somedata")
from {{cookiecutter.module_name}}.api import somedata  # noqa: E402,F401
{% endif %}
{%- if cookiecutter.ui_blueprint | lower == 'y' %}

# UI
{{cookiecutter.module_name}}_ui_bp: Blueprint = Blueprint(
    "{{cookiecutter.plugin_name}} UI",
    __name__,
    template_folder="ui/templates",
    url_prefix="/{{cookiecutter.plugin_slug}}"
)
ensure_bp_routes_are_loaded_fresh("ui.views.dashboards")
from {{cookiecutter.module_name}}.ui.views import dashboard  # noqa: E402,F401
{% endif %}
{%- if cookiecutter.cli_blueprint | lower == 'y' %}

# CLI
{{cookiecutter.module_name}}_cli_bp: Blueprint = Blueprint("{{cookiecutter.plugin_name}}", __name__)
{{cookiecutter.module_name}}_cli_bp.cli.help = "{{cookiecutter.plugin_name}} CLI commands"
ensure_bp_routes_are_loaded_fresh("cli.commands")
from {{cookiecutter.module_name}}.cli import commands  # noqa: E402,F401
{% endif %}
