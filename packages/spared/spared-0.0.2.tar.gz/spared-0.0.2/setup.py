import setuptools
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="spared",
    version="0.0.2",
    author="Gabriel Mejia",
    author_email="gm.mejia@uniandes.edu.co",
    description="This package runs all the functions for SPaRED and Spackle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dvegaa00/Library_Spared_Spackle/tree/main",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where="spared", exclude=["tests", "tests.*", 
                                                    "gtftools.py", 
                                                    "data", "data.*", 
                                                    "configs", "configs.*", 
                                                    "imput_results", "imput_results.*", 
                                                    "lightning_logs", "lightning_logs.*", 
                                                    "processed_data", "processed_data.*", 
                                                    "PublicDatabase", "PublicDatabase.*",
                                                    "readers", "readers.*",
                                                    "spackle", "spackle.*",
                                                    ]),
    package_dir={"": "spared"},
    python_requires=">=3.7",
)

