# CookieCutter templates for FlexMeasures plugins

This template helps you to rapidly get ready to add custom functionality to FlexMeasures, with a full-fledged Python package with

- Several Blueprints prepared to add functionality right away (e.g. for UI views, API endpoints, CLI commands)
- Professional coding practices (see below on conventions)

If you want something simpler, we describe a one-file approach [here](https://flexmeasures.readthedocs.io/en/latest/plugin/showcase.html).


## Usage

```
pip install cookiecutter
cookiecutter https://github.com/FlexMeasures/flexmeasures-plugin-template
```

This will ask you about your project name etc.

The result is a directory, which can be used as a starting point for a FlexMeasures plugin.

You are asked if you need one or more of three blueprints and sub-packages installed, "api", "ui" and "cli". These are the cornerstones of pluggable functionality in FlexMeasures plugins.
You can remove any of them later (remove the folder and also the blueprint initialization from `__init__.py`).

For more info on FlexMeasures plugin development, see also [the FlexMeasures documentation on plugins](https://flexmeasures.readthedocs.io/en/latest/plugin/introduction.html).


## Conventions

We are using some opinionated conventions which stem from our work on FlexMeasures. You are free to ignore / delete or change them, of course.

- Code hygiene: We add flake8, black and mypy checks/corrections. We automate them using pre-commit.
- We bundle requirements per "app", "dev" and "test". See the Makefile for some handy targets for managing requirements.
- We use setuptools_scm for versioning and to detect sub-packages. Versions thus come from git tags (also dev-versions).


## Getting FlexMeasures to load your plugin

You have two options for FlexMeasures to recognize your plugin when starting (e.g. with `flexmeasures run` or any other command):

- point the config setting `FLEXMEASURES_PLUGINS` to the module folder (containing the `__init__.py` file). Both relative or absolute paths work.
- install your plugin as a Python package (e.g. `python setup.py install` or even `pip install <your_package>` in case you distribute it). For FlexMeasures to load it, the `FLEXMEASURES_PLUGINS` setting to add is the module name.

The first option (pointing to the directory) probably works best, especially for early development. As for a version, FlexMeasures will assume it to be "Unknown", unless you also give it a minimal git setup (as we describe below). Alternatively, you can also edit `__init__.py` and set the version there. 

We'll talk more about the second option in the next section. 

## Installing your plugin 

The second option from the section above (installation) requires some more attention.

First, `cd` into your new plugin directory.

And probably you want a virtual environment to keep installed dependencies in:

```
python3 -m venv venv-for-my-plugin  # or whatever you are using to create virtual environments
source venv-for-my-plugin/bin/activate  # in the above method, you'd activate like this
```

### (git) version

You need to set up a basic git history, so setuptools_scm (see our conventions above) can know your version and also find packages. 

Here is an example of a minimal setup with a freshly created plugin directory:

```
git init
git add Readme.md
git commit -am "add Readme"
git tag -a "v0.1.0"
```

If you don't want to use setuptools_scm, edit `setup.py`.


### Install dependencies and your plugin

You could now run `make install-for-dev` (which installs dependencies and then your plugin via `python setup.py develop`) and then find something like this when you call `pip list`:

```
flexmeasures-testplugin 0.1.0      /your/path/to/flexmeasures-testplugin
```

Note that you wouldn't need to install FlexMeasures seperately, as FlexMeasures is now a dependency of your plugin :) The FlexMeasures version you selected during the initial setup is a minimum, and if you install FlexMeasures, pip will be free to select the latest. If you want the exact version, change ``>=`` in `requirements/app.in` to `==`.

You can add other dependencies of yours in `requirements/app.in`. Actually, even other FlexMeasures plugins could become dependencies of your plugin (if they have been distributed on Pypi). Very useful if you depend on certain data integrations.


### Run tests

One final step could be to run your tests:

```
pytest
```

We included a few dummy tests for you to overwrite.


## Publishing your plugin

To make your work publicly available (and also pip-installable), publish it to Pypi.
We suggest going through the above section to install your plugin locally first.

Here is the necessary code you should run:

```
rm -rf build/* dist/*
pip -q install twine
pip -q install wheel

python setup.py egg_info sdist
python setup.py egg_info bdist_wheel

twine upload dist/*
```

All you need is a Pypi account configured.
The version of your package will depend on the git tag (see above).
