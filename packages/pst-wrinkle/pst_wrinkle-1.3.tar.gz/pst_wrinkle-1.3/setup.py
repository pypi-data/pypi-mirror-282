from setuptools import setup, find_packages

setup(
    name='pst_wrinkle',
    version='2.0',
    packages=find_packages(),
    install_requires=[
        'wget',
        'igv_notebook',  
        'matplotlib',
        'cartopy',
        'geopandas',
        'numpy',
        'pandas'
    ],
)