# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name='redis-cluster-python',
    version='0.0.2',
    description='This is my ctrip help package',
    long_description='This is my ctrip help package',
    author='ckf10000',
    author_email='ckf10000@sina.com',
    url='https://github.com/ckf10000/ctrip-helper',
    packages=find_packages(),
    install_requires=[
        'redis>=5.0.7'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
