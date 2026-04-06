from setuptools import setup


def load_requirements():
    """
    Loading (extra) requirements for this plugin.

    There should not be conflicts with FlexMeasures coming from here.
    We should only add requirements which FlexMeasures does not depend on already.
    """
    reqs = []
    with open("requirements.txt", "r") as f:
        reqs = [
            req
            for req in f.read().splitlines()
            if not req.strip() == ""
            and not req.strip().startswith("#")
            and not req.strip().startswith("-c")
            and not req.strip().startswith("--find-links")
        ]
    return reqs


setup(install_requires=load_requirements())
