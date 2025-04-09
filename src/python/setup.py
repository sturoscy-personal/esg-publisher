#!/usr/bin/env python

import configparser as cfg
import os
import sys
from pathlib import Path
from shutil import copyfile

import esgcet
from setuptools import find_packages, setup

VERSION = esgcet.__version__

additional_requirements = ["xarray", "netcdf4", "dask", "pyyaml", "globus-sdk"]


setup(
    name="esgcet",
    version=VERSION,
    description="ESGCET publication package",
    author="Sasha Ames",
    author_email="ames4@llnl.gov",
    url="http://esgf.llnl.gov",
    install_requires=[
        "requests",
        "esgfpid",
        "ESGConfigParser==1.0.0a1",
    ]
    + additional_requirements,
    packages=find_packages(exclude=["ez_setup"]),
    include_package_data=True,
    zip_safe=False,  # Migration repository must be a directory
    entry_points={
        "console_scripts": [
            "esgpidcitepub=esgcet.esgpidcitepub:main",
            "esgmkpubrec=esgcet.esgmkpubrec:main",
            "esgindexpub=esgcet.esgindexpub:main",
            "esgpublish=esgcet.pub_internal:main",
            "esgupdate=esgcet.esgupdate:main",
            "esgmapconv=esgcet.esgmapconv:main",
            "esgmigrate=esgcet.migratecmd:main",
            "esgunpublish=esgcet.esgunpublish:main",
            "esgstacpub=esgcet.esgstacpub:main",
        ]
    },
)
