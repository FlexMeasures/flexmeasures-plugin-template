# {{cookiecutter.plugin_name}} - a plugin for FlexMeasures


## Usage


## Installation

1. Add "{{cookiecutter.module_name}}" to your FlexMeasures (>v0.7.0) config file,
   using the FLEXMEASURES_PLUGINS setting (a list).

2.  


## Development

We use pre-commit to keep code quality up:

    pip install pre-commit black flake8 mypy
    pre-commit install
    pre-commit run --all-files --show-diff-on-failure
