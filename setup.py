#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versiontools_support
from setuptools import setup, find_packages

setup(
    name = 'taiga-contrib-google-auth-x',
    version = ":versiontools:taiga_contrib_google_auth_x:",
    description = "The Taiga plugin for google authentication",
    long_description = "",
    keywords = 'taiga, google, auth, plugin',
    author = 'erTho',
    author_email = 'ertho@bitconseil.fr',
    url = 'https://github.com/er-tho/taiga-contrib-google-auth-x',
    license = 'AGPL',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[],
    setup_requires = [
        'versiontools >= 1.9',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
