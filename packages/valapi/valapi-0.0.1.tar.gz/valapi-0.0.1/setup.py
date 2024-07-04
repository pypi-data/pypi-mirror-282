from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_desc = fh.read()

setup(
    name="valapi",
    version="0.0.1",
    author="qzenna",
    description="Wrapper for VALORANT's client API",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/mela-nen/VALC/",
    project_urls={
        "Bug Tracker": "https://github.com/mela-nen/VALC/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)