"""Python setup.py for ECS Helm Utilities package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.1'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="ecs_helm_utilities",
    version="0.1.1",
    description="Utilities to work with Helm Charts",
    url="https://gitlab.com/emergent-community-systems/ecs-helm-utilities",
    long_description="Utilities to work with Helm Charts",
    long_description_content_type="text/markdown",
    author="Jaime Magiera",
    packages=find_packages()
)
