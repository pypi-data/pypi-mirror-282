import re
import shutil
import subprocess
import sys
import os
import compileall
from setuptools import setup, find_packages

"""python setup.py bdist_wheel"""
"""python setup.py bdist"""

VERSION = "0.0.0"
DESCRIPTION = "Python for Ternion development"
LONG_DESCRIPTION = "Python fot Ternion development"
setup(
    name="pythonion",
    version=VERSION,
    author="Santi Nuratch",
    author_email="santi.inc.kmutt@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    package_data={
        #
    },
    include_package_data=True,
    install_requires=[
        "pyserial",
        "colorlog",
        "customtkinter",
    ],
    keywords=["python", "pythonion", "ternion"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)

"""python setup.py bdist_wheel"""
