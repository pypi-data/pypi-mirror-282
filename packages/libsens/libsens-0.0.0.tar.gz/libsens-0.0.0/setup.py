from setuptools import setup, find_packages

setup(
    name="libsens",
    version="0.0.0",
    description="Libsens library",
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.10',
    include_package_data=True,
    install_requires = open('requirements.txt').readlines(),
)
