#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='site-scalper',
    version='0.0.1',
    description='String based website scalper and auto-email system',
    long_description='Automated Gmail-email alert from scalping a website over a defined time period',
    long_description_content_type="text/markdown",
    author='Ed Harrison',
    author_email='eh@emrld.no',
    url='https://github.com/eddjharrison/site-scalper',
    packages=setuptools.find_packages(),
    install_requires=[
            "googleapiclient",
            "google"
    ],
    entry_points={
        'console_scripts': [
            'site-sclaper = site_scalper:main',
        ],
    },
)
