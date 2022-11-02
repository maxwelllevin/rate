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
    package_data={
        "inputs": [
            "C2H2_g.txt",
            "C2H4_g.txt",
            "CH4_g.txt",
            "C0_g.txt",
            "C02_g.txt",
            "H_g.txt",
            "H2_g.txt",
            "H2O_g.txt",
            "HCN_g.txt",
            "N2_g.txt",
            "NH3_g.txt",
        ]
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy", "scipy"],
)
