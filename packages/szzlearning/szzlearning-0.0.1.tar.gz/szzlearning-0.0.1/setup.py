from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
name="szzlearning",
version="0.0.1",
author = "Author's name",
description="Description's package",
packages=["szzlearning"]
)
