import setuptools  # type: ignore
from pathlib import Path

setuptools.setup(
    name="thanhpdf",
    version="1.0",
    long_description="",
    packages=setuptools.find_packages(exclude=["test", "data"])
)