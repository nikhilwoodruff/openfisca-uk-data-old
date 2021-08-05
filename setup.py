from setuptools import setup, find_packages

setup(
    name="openfisca-data",
    version="0.1.1",
    description=("A Python package to manage OpenFisca-compatible microdata"),
    url="http://github.com/ubicenter/openfisca-data",
    author="Nikhil Woodruff",
    author_email="nikhil.woodruff@outlook.com",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pathlib",
        "tqdm",
        "tables",
        "h5py",
        "synthimpute @ git+https://github.com/PSLmodels/synthimpute",
    ],
    entry_points={
        "console_scripts": ["openfisca-data=openfisca_data.cli:main"],
    },
)
