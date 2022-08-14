#!/usr/bin/env python

from setuptools import find_packages, setup

packages = ["inspirationq." + p for p in find_packages("inspirationq")]

setup(
    name="Inspiration-Q API",
    version="0.1",
    description="Inspiration-Q API Python interface",
    url="https://www.inspiration-q.com/",
    packages=["inspirationq"] + packages,
)

