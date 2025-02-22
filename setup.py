#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 B-Open Solutions srl - http://bopen.eu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import codecs
import os

from setuptools import find_packages, setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


version = '0.9.9.dev0'

setup(
    name='elevation',
    version=version,
    author='B-Open Solutions srl, Alessandro Amici',
    author_email='info@bopen.eu',
    license='Apache License Version 2.0',
    url='http://elevation.bopen.eu',
    download_url='https://github.com/bopen/elevation/archive/%s.tar.gz' % version,
    description="Python script to download global terrain digital elevation models, "
                "SRTM 30m DEM and SRTM 90m DEM.",
    long_description=read('README.rst'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'future',
        'appdirs',
        'fasteners',
        'click',
    ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    keywords='script download SRTM DEM DTM global digital elevation terrain model',
    entry_points={
        'console_scripts': ['eio=elevation.cli:eio'],
    },
)
