"""

pythonion_root
pythonion_root/
    ├── pythonion/
    │   ├── __init__.py
    │   ├── logs/
    │   │   └── __init__.py
    │   ├── link/
    │   │   └── __init__.py
    │   └── uart/
    │       └── __init__.py
    ├── setup.py
    └── main.py

"""

"""

python -m compileall pythonion

python setup.py sdist bdist_wheel
pip install twine
twine upload dist/*
pip install pythonion
from pythonion import logs, link, uart
"""

import os
import shutil
from setuptools import setup, find_packages


def text_space(text: str, length: int = 20):
    t = text
    if len(text) < length:
        t = t + " " * (length - len(text))
    return t


def move_pyc_files(root_dir):
    print("")
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".pyc"):
                pyc_path = os.path.join(root, file)
                target_dir = root.replace("__pycache__", "").rstrip(os.sep)
                target_file = os.path.join(
                    target_dir, file.split(".")[0] + ".pyc"
                )
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(pyc_path, target_file)
                print(
                    f"Moved {text_space(pyc_path.replace(root_dir, ''))} -> {target_file.replace(root_dir, '')}"
                )


current_directory = os.path.dirname(__file__)
pythonion_dir = os.path.join(current_directory, "pythonion")
move_pyc_files(pythonion_dir)
print("done")

setup(
    name="pythonion",
    version="0.0.1",
    author="Ternion Development Team",
    author_email="santi.inc.kmutt@example.com",
    description="Python package for Ternion microcontroller board",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/drsanti/pythonion",
    packages=find_packages(),
    package_data={
        "": ["*.pyc"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.10",
    install_requires=[
        # List your package dependencies here
    ],
)
