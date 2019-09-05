#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: dayudada
# Mail: dayudada@foxmail.com
# Created Time: 2019-9-5 18:10:34
#############################################


import setuptools

with open('README.md','r',encoding='UTF-8') as f:
    long_description = f.read()
    
setuptools.setup(
    name="ucms",
    version="1.0.0",
    keywords=("ucms"),
    description="UCMS采集接口python推送库,用于python将采集内容推送到UCMS上",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    url="https://github.com/dayudada/ucms_caiji_python",
    author="dayudada",
    author_email="dayudada@foxmail.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    platforms="any",
    install_requires=[
        'requests'
    ]
)
