import pathlib

import setuptools

setuptools.setup(
    name="love_equinox",
    version="0.2.2",
    description="Module to calculate love equinox",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/normthenord/love_equinox",
    author="Normthenord",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires =">=3.10, <3.14",
    packages=setuptools.find_packages(),
    include_package_data=True,
)