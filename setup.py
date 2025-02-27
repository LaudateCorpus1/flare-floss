#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2017 Mandiant, Inc. All Rights Reserved.

import os

import setuptools

requirements = [
    "tabulate==0.8.9",
    "vivisect==1.0.5",
    "viv-utils[flirt]==0.6.9",
    "pydantic==1.8.2",
    "tqdm==4.62.3",
    "networkx==2.5.1",
    "halo==0.0.31",
]

# this sets __version__
# via: http://stackoverflow.com/a/7071358/87207
# and: http://stackoverflow.com/a/2073599/87207
with open(os.path.join("floss", "version.py"), "r") as f:
    exec(f.read())


# via: https://packaging.python.org/guides/making-a-pypi-friendly-readme/
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), "r") as f:
    long_description = f.read()


setuptools.setup(
    name="flare-floss",
    version=__version__,
    description="FLARE Obfuscated String Solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Willi Ballenthin, Moritz Raabe",
    author_email="william.ballenthin@mandiant.com, moritz.raabe@mandiant.com",
    url="https://www.github.com/mandiant/flare-floss",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_dir={"floss": "floss"},
    entry_points={
        "console_scripts": [
            "floss=floss.main:main",
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        "dev": [
            "pyyaml==6.0",
            "pytest==6.2.5",
            "pytest-sugar==0.9.4",
            "pytest-instafail==0.4.2",
            "pytest-cov==3.0.0",
            "pycodestyle==2.8.0",
            "black==21.11b1",
            "isort==5.10.1",
            "mypy==0.910",
            # type stubs for mypy
            "types-backports==0.1.3",
            "types-colorama==0.4.4",
            "types-PyYAML==6.0.1",
            "types-tabulate==0.8.3",
            "types-termcolor==1.1.2",
        ],
        "build": [
            "pyinstaller==4.7",
        ],
    },
    zip_safe=False,
    keywords="floss malware analysis obfuscation strings FLARE",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
    ],
    python_requires=">=3.6",
)
