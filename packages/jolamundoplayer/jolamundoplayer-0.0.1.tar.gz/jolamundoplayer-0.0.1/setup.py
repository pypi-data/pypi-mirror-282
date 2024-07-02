import setuptools
from pathlib import Path


archivo = Path(r"README.md")
long_desc = archivo.read_text("utf-8")
setuptools.setup(
    name="jolamundoplayer",
    version="0.0.1",
    long_description=long_desc,
    packages=setuptools.find_packages(
        exclude=["mocks", "test"]
    )
)
