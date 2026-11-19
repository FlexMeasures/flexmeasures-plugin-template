import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'


module_name = "{{ cookiecutter.module_name }}"

if not re.match(MODULE_REGEX, module_name):
    print(f"ERROR: {module_name} is not a valid Python module name. Probably you need to remove special characters.")
    sys.exit(1)



# FlexMeasures refuses automation type IDs that do not match this pattern when it loads the plugin.
AUTOMATION_TYPE_REGEX = r'^[a-z][a-z0-9_-]{0,79}$'

if "{{ cookiecutter.automation | lower }}" == "y":
    automation_type = "{{ cookiecutter.plugin_slug }}-example"
    if not re.match(AUTOMATION_TYPE_REGEX, automation_type):
        print(
            f"ERROR: {automation_type} is not a valid automation type ID."
            " Use a plugin slug of lowercase letters, digits, underscores or hyphens, starting with a letter."
        )
        sys.exit(1)

    # Automation types from plugins arrived in FlexMeasures v1.1.0.
    minimal_version = "{{ cookiecutter.minimal_flexmeasures_version }}"
    version_match = re.match(r'^(\d+)\.(\d+)', minimal_version)
    if minimal_version and (not version_match or tuple(map(int, version_match.groups())) < (1, 1)):
        print(f"ERROR: automation types require FlexMeasures v1.1.0 or later, not {minimal_version}.")
        sys.exit(1)
