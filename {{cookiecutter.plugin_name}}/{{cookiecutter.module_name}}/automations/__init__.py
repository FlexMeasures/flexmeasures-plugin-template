"""
Automation types this plugin adds to FlexMeasures (requires FlexMeasures >= 1.1.0).

FlexMeasures reads `__automation_types__` from the plugin's `__init__`, which imports it from here.
Pick the type ID before anyone creates an automation with it: stored automations refer to it.
Read credentials from FlexMeasures config settings, never from the automation's configuration or parameters, which are stored.
"""

from flexmeasures.data.automations import AutomationHandler

from .generator import {{ cookiecutter.module_name|replace('_', ' ')|title|replace(' ', '') }}Generator

__automation_types__ = [
    AutomationHandler(
        # A lowercase slug that identifies the type; stored automations refer to it.
        type_id="{{ cookiecutter.plugin_slug }}-example",
        # The name of this type's tab on the automations page: a short, capitalized title, e.g. "Weather forecast import".
        display_name="Example: input × factor",
        generator_class={{ cookiecutter.module_name|replace('_', ' ')|title|replace(' ', '') }}Generator,
        queue="ingestion",
        result_noun="measurement",
    )
]
