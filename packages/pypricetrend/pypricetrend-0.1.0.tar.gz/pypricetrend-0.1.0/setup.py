# setup.py

from setuptools import setup, find_packages

setup(
    name='pypricetrend',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        "scikit-learn",
        "matplotlib",
    ],
    author='Dominic Plouffe',
    author_email='dominic@dplouffe.ca',
    description='The `pypricetrend` package provides tools to analyze and forecast product demand based on historical sales data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dominicplouffe/pypricetrend',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)