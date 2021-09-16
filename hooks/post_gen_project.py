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