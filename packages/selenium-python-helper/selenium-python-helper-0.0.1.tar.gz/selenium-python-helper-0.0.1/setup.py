# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  selenium-python-helper
# FileName:     setup.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/06/28
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""

from setuptools import setup, find_packages

setup(
    name='selenium-python-helper',
    version='0.0.1',
    description='This is my selenium help package',
    long_description='This is my selenium help package',
    author='ckf10000',
    author_email='ckf10000@sina.com',
    url='https://github.com/ckf10000/selenium-python-helper',
    packages=find_packages(),
    install_requires=[
        'psutil>=5.9.8',
        'requests>=2.31.0',
        'selenium>=4.21.0',
        'pypinyin>=0.51.0',
        'selenium-wire>=5.1.0',
        'webdriver-manager>=4.0.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
