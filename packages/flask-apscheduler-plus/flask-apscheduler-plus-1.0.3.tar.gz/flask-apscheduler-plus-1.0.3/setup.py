# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name='flask-apscheduler-plus',
    version='1.0.3',
    description='This is my flask apscheduler package',
    long_description='This is my flask apscheduler package',
    author='ckf10000',
    author_email='ckf10000@sina.com',
    url='https://github.com/ckf10000/flask-apscheduler-plus',
    packages=find_packages(),
    install_requires=[
        "six>=1.16.0",
        "pytz>=2022.1",
        "werkzeug>=3.0.3",
        "flask>=3.0.3",
        "apscheduler>=3.9.1",
        "redis-cluster-python>=0.0.2",
        "python-dateutil>=2.9.0.post0"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
