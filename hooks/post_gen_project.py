import os
from shutil import rmtree

REMOVE_PATHS = [
    '{% if cookiecutter.api_blueprint | lower != "y" %} {{cookiecutter.module_name}}/api {% endif %}',
    '{% if cookiecutter.ui_blueprint | lower != "y" %} {{cookiecutter.module_name}}/ui {% endif %}',
    '{% if cookiecutter.cli_blueprint | lower != "y" %} {{cookiecutter.module_name}}/cli {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            rmtree(path)
        else:
            os.unlink(path)

# Show the user the FLEXMEASURES_PLUGINS path
plugin_path = os.path.join(os.getcwd(), "{{cookiecutter.module_name}}")
print(
    f"\nSuccess! Your plugin '{{cookiecutter.plugin_name}}' has been created.\n"
    f"\nTo load this plugin, add the following path to your FlexMeasures config:\n"
    f"\n    FLEXMEASURES_PLUGINS = [\"{plugin_path}\"]\n"
)