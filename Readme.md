# CookieCutter templates for FlexMeasures plugins

## Usage

```
pip install cookiecutter
cookiecutter https://github.com/SeitaBV/flexmeasures-plugin-template
```

This will ask you about your project name etc ...

The plugin_name, plus the prefix "flexmeasures-" will be used for your directory, which we recommend as a naming convention.
Likewise, the prefix "flexmeasures_" wil be used to define the package name.

The result is a directory which can be used as a starting point for a FlexMeasures plugin.

You will get three blueprints and sub-packages installed, "api", "ui" and "cli". These are the cornerstones of pluggable functionality in FlexMeasures plugins.
You can remove any of them.  TODO: make this a selective process when creating the project.


For more info on FlexMeasures plugin development, see also [the FlexMeasures documentation on plugins](https://flexmeasures.readthedocs.io/en/latest/dev/plugins.html).


## Conventions

We are using some conventions which stem from our work on FlexMeasures. You are free to ignore / delete or change of course.

- Code hygiene: We add flake8, black and mypy checks/corrections. We automate them using pre-commit.
- We bundle requirements per "app", "dev" and "test". See the Makefile for some handy targets for managing requirements.
- We use setuptools_scm for versioning. Versions come from git tags.
