from setuptools import find_packages, setup

with open("README.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="bootloader_flashing",
    version="0.1.3",
    description="utils for flashing bootloader",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    url="https://github.com/my-python-utils/bootloader_flashing",
    packages=find_packages(exclude=("tests",)),
    license="MIT License",
)
