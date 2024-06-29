# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name="redis-cluster-python",
    version="0.0.1",
    author="ZhouHanLin",
    author_email="zhhlvip@sina.com",
    description="Python Framework.",
    license="MIT",
    url="",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=True,
    platforms='any',
    install_requires=[
        "redis==4.3.6"
    ],
)
