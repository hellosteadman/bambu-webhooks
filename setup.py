#!/usr/bin/env python
from setuptools import setup
from os import path

setup(
    name = 'bambu-webhooks',
    version = '2.0',
    description = 'Create webhooks and allow users to assign URLs to them',
    author = 'Steadman',
    author_email = 'mark@steadman.io',
    url = 'https://github.com/iamsteadman/bambu-webhooks',
    long_description = open(path.join(path.dirname(__file__), 'README')).read(),
    install_requires = [
        'Django>=1.4',
        'requests',
        'bambu-cron>=2.0'
    ],
    packages = [
        'bambu_webhooks',
        'bambu_webhooks.migrations'
    ],
    package_data = {
        'bambu_webhooks': [
            'templates/webhooks/*.html'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django'
    ]
)