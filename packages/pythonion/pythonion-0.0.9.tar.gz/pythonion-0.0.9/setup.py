"""

pythonion_root/
├── deploy/
│   └── pythonion/
│       ├── __init__.pyc
│       ├── logs/
│       │   ├── __init__.pyc
│       │   └── logs.pyc
│       ├── link/
│       │   ├── __init__.pyc
│       │   └── link.pyc
│       └── uart/
│           ├── __init__.pyc
│           │
│           └── uart.pyc
├── dist/
│   ├── pythonion-0.0.5-py3-none-any.whl
│   └── pythonion-0.0.5.tar.gz
│
├── pythonion/
│   ├── __init__.py
│   ├── logs/
│   │   ├── __init__.py
│   │   └── logs.py
│   ├── link/
│   │   ├── __init__.py
│   │   └── link.py
│   └── uart/
│       ├── __init__.py
│       └── uart.py
│
├── setup.py
├── main.py
└── README.md


"""

"""

1) Change directory to pythonion_root
    cd pythonion_root
    
2) Update version number
    version="0.0.X", 
    
    rm -rf build && rm -rf deploy  && rm -rf dist

3) Compile:
        python -m compileall ./pythonion
        
4)  Build Package:    
        python setup.py sdist bdist_wheel
        
5)  Upload Package:
        (optional) pip install twine
        
        twine upload dist/*

        (input the token)
token:
pypi-AgEIcHlwaS5vcmcCJDQ1YzBlMzY3LWVjZDktNGMyNC1iNmVjLTM2ZGNlYzY2MzBiMQACKlszLCI3M2Q0Y2UxZi00ZGJlLTRkOGYtYTYwYi0zMDhjODlhZjUzZTYiXQAABiBohzNnbR4qMWm54fgG36tLq3uMCztn2O_XTOYtMKLBoQ



6)  Install Package:
    python -m pip install pythonion
    
7)  Install Package Locally:
    python setup.py install




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


def text_space(text: str, length: int = 50):
    t = text
    if len(text) < length:
        t = t + " " * (length - len(text))
    return t


def move_pyc_files(src_root, dst_root):
    print("")
    for root, dirs, files in os.walk(src_root):
        for file in files:
            if file.endswith(".pyc"):
                pyc_path = os.path.join(root, file)
                # Create the target directory by replacing the source root with the destination root
                target_dir = root.replace(src_root, dst_root)

                # Remove the suffix `__pycache__` from the `target_dir`
                # target_dir = target_dir.replace(f"{os.sep}__pycache__", "")

                os.makedirs(target_dir, exist_ok=True)
                target_file = os.path.join(
                    target_dir, file.split(".")[0] + ".pyc"
                )
                shutil.move(pyc_path, target_file)
                print(
                    f"Moved {text_space(pyc_path.replace(src_root, ''))} -> {target_file.replace(src_root, '')}"
                )


current_dir = os.path.dirname(__file__)

# */pythonion_root/pythonion
src_root = os.path.join(current_dir, "pythonion")

# */pythonion_root/deploy/pythonion
dst_root = os.path.join(current_dir, "deploy", "pythonion")

move_pyc_files(src_root, dst_root)
print("done")


setup(
    name="pythonion",
    version="0.0.9",
    author="Ternion Development Team",
    author_email="santi.inc.kmutt@example.com",
    description="Python package for Ternion microcontroller board",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/drsanti/pythonion",
    packages=find_packages(
        where="deploy"
    ),  # Include packages from 'deploy' directory
    include_package_data=True,  # Include all package data, including *.pyc files
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.10",
    install_requires=[
        "pyserial",
        "colorlog",
        "customtkinter",
        # List your package dependencies here
    ],
)

# setup(
#     name="pythonion",
#     version="0.0.8",
#     author="Ternion Development Team",
#     author_email="santi.inc.kmutt@example.com",
#     description="Python package for Ternion microcontroller board",
#     long_description=open("README.md").read(),
#     long_description_content_type="text/markdown",
#     url="https://github.com/drsanti/pythonion",
#     package_dir={"": "deploy"},
#     packages=find_packages(where="deploy"),  # Use 'deploy' as the root
#     include_package_data=True,  # Ensure package data is included
#     package_data={"": ["*.pyc"]},  # Specify to include .pyc files
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "Operating System :: Microsoft :: Windows",
#     ],
#     python_requires=">=3.10",
#     install_requires=[
#         "pyserial",
#         "colorlog",
#         "customtkinter",
#         # List your package dependencies here
#     ],
# )
