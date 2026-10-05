# {{cookiecutter.plugin_name}} - a plugin for FlexMeasures


## Usage


## Installation

1. Add "/path/to/{{cookiecutter.plugin_name}}/{{cookiecutter.module_name}}" to your FlexMeasures (>v0.7.0dev8) config file,
   using the FLEXMEASURES_PLUGINS setting (a list).
   Alternatively, if you installed this plugin as a package (e.g. via `python setup.py install`, `pip install -e` or `pip install {{cookiecutter.module_name}}` should this project be on Pypi), then "{{cookiecutter.module_name}}" suffices.

2.  
{% if cookiecutter.automation | lower == 'y' %}

## Automations

This plugin adds the automation type `{{cookiecutter.plugin_slug}}-example` to FlexMeasures (which requires FlexMeasures v1.1.0 or later).
On each run, it records a value on the configured sensor for the current time slot:
the `offset` parameter, plus `factor` times the latest value of the input sensor, if one is configured.
Its data generator lives in `{{cookiecutter.module_name}}/automations/generator.py`, ready to be replaced by your own computation.

Create an automation for an asset, with a configuration file naming the sensors:

    echo '{"sensor": <output sensor ID>, "input-sensor": <input sensor ID>}' > config.json
    echo '{"offset": 0, "factor": 1}' > parameters.json
    flexmeasures add automation --asset <asset ID> --name "Example" --type {{cookiecutter.plugin_slug}}-example \
        --cron "*/15 * * * *" --config config.json --parameters parameters.json

The output sensor must belong to that asset or one of its descendants.
The input sensor is optional.

Run the automation once, and work on the queue its jobs go to:

    flexmeasures jobs run-automation --automation <automation ID>
    flexmeasures jobs run-worker --queue ingestion

The worker needs this plugin loaded too.
From then on, `flexmeasures jobs run-automations` (e.g. run by cron) queues a run whenever the automation is due.

When you change what the generator computes, bump its `__version__`,
and recreate the automations of this type; FlexMeasures refuses to run an automation created with another version.
Read credentials from FlexMeasures config settings, never from an automation's configuration or parameters, as those are stored.
See [the FlexMeasures documentation on plugin automation types](https://flexmeasures.readthedocs.io/latest/plugin/customisation.html#plugin-automation-types).
{% endif %}

## Development

We use pre-commit to keep code quality up.

Install necessary tools with:

    pip install pre-commit black flake8 mypy
    pre-commit install

or:

    make install-for-dev

Try it:

    pre-commit run --all-files --show-diff-on-failure
