#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time: 2018-1-23 19:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name="ucms",
    version="0.1.0",
    keywords=("ucms"),
    description="UCMS采集接口python推送库,用于python将采集内容推送到UCMS上",
    long_description="UCMS采集接口python推送库,用于python将采集内容推送到UCMS上,使用方法请访问https://github.com/dayudada/ucms_caiji_python",
    license="MIT Licence",

    url="https://github.com/dayudada/ucms_caiji_python",
    author="dayudada",
    author_email="dayudada@foxmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        'requests'
    ]
)
