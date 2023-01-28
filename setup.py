#!/usr/bin/env python

from distutils.core import setup

setup(
    name="rate",
    version="1.0.0",
    description="Reliable Analytic Thermochemical Equilibrium",
    author="Patricio Cubillos",
    author_email="patricio.cubillos@oeaw.ac.at",
    url="https://github.com/pcubillos/rate/",
    packages=["rate"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy", "scipy"],
)
