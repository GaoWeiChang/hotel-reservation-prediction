from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="HOTEL_RESERVATION_PREDICTION",
    version=0.1,
    author="Thomas",
    packages=find_packages(), # find __init__.py(package) file in those folders
    install_requires = requirements,
)