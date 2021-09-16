"""
The __init__ for the {{cookiecutter.plugin_name}} FlexMeasures plugin.
"""

__version__ = "Unknown version"


from importlib_metadata import version, PackageNotFoundError

from flask import Blueprint


# This uses importlib.metadata behaviour added in Python 3.8
# and relies on setuptools_scm.
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
from {{cookiecutter.module_name}}.ui.views import dashboard  # noqa: E402,F401
{% endif %}
{%- if cookiecutter.cli_blueprint | lower == 'y' %}

# CLI
{{cookiecutter.module_name}}_cli_bp: Blueprint = Blueprint("{{cookiecutter.plugin_name}}", __name__)
{{cookiecutter.module_name}}_cli_bp.cli.help = "{{cookiecutter.plugin_name}} CLI commands"
from {{cookiecutter.module_name}}.cli import commands  # noqa: E402,F401
{% endif %}
