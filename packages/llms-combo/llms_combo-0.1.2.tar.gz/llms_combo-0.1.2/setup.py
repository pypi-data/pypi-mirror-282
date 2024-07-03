#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/3 上午9:34
# @Author  : haochonglei
# @File    : setup.py
# @Software: PyCharm
from setuptools import setup, find_packages

setup(
    name="llms_combo",
    version="0.1.2",
    author="Jared Hao",
    author_email="9190632@qq.com",
    description="A simple example package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
