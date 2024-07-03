from setuptools import setup, find_packages

setup(
    name='pst_wrinkle',
    version='1.2',
    packages=find_packages(),
    install_requires=[
        'wget',
        'malariagen-data',
        'igv_notebook',  
        'matplotlib',
        'cartopy',
        'geopandas',
        'numpy',
        'pandas'
    ],
)