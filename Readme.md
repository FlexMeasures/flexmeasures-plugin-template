# CookieCutter templates for FlexMeasures plugins

This template helps you to rapidly get ready to add custom functionality to FlexMeasures, with a full-fledged Python package with

- Several Blueprints prepared to add functionality right away (e.g. for UI views, API endpoints, CLI commands)
- Professional coding practices (see below on conventions)

If you want something simpler, we describe a one-file approach [here](https://flexmeasures.readthedocs.io/en/latest/dev/plugins.html).


## Usage

```
pip install cookiecutter
cookiecutter https://github.com/SeitaBV/flexmeasures-plugin-template
```

This will ask you about your project name etc.

The result is a directory, which can be used as a starting point for a FlexMeasures plugin.

You will get three blueprints and sub-packages installed, "api", "ui" and "cli". These are the cornerstones of pluggable functionality in FlexMeasures plugins.
You can remove any of them (remove the folder and also the blueprint initialization from `__init__.py`).  

For more info on FlexMeasures plugin development, see also [the FlexMeasures documentation on plugins](https://flexmeasures.readthedocs.io/en/latest/dev/plugins.html).


## Conventions

We are using some opinionated conventions which stem from our work on FlexMeasures. You are free to ignore / delete or change them, of course.

- Code hygiene: We add flake8, black and mypy checks/corrections. We automate them using pre-commit.
- We bundle requirements per "app", "dev" and "test". See the Makefile for some handy targets for managing requirements.
- We use setuptools_scm for versioning and to detect sub-packages. Versions thus come from git tags (also dev-versions).


## Getting FlexMeasures to load your plugin / versioning

You have two options for FlexMeasures to recognize your plugin when starting (e.g. with `flexmeasures run` or any other command):

- point the config setting `FLEXMEASURES_PLUGINS` to the module folder (containing the `__init__.py` file). Both relative or absolute paths work.
- install your plugin as a Python package (e.g. `python setup.py install` or `pip install <your_package>`). For FlexMeasures to load it, the `FLEXMEASURES_PLUGINS` setting to add is the module name.

The second option (installation) requires setting up a basic git history, so setuptools_scm (see above) can know your version and also find packages. 

Here is an example of a minimal setup with a freshly created directory:

```
git init
git add Readme.md
git commit -am "add Readme"
git tag -a "v0.1.0"
python setup.py install
```

An interesting part to note about the second option is that you wouldn't need to install FlexMeasures, as FlexMeasures is a dependency of your plugin :)
And of course, other plugins can become dependencies of your plugin, as well. Very useful if you depend on certain data integrations.

The first option (pointing to the directory) means that your package will have a version of "Unknown" unless you also give it a minimal git setup as above. Alternatively, you can also edit `__init__.py` and set the version there. 


## Publishing your plugin

To make your work publicly available (and also pip-installable), publish to Pypi with this method:

```
rm -rf build/* dist/*
pip -q install twine
pip -q install wheel

python setup.py egg_info sdist
python setup.py egg_info bdist_wheel

twine upload dist/*
```

All you need is a Pypi account configured.
