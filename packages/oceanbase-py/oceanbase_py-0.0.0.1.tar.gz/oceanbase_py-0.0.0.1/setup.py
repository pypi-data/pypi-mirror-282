#! /usr/bin/python3

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import ast
import re

from setuptools import find_packages, setup

package_name = "oceanbase_py"
_version_re = re.compile(r"__version__\s+=\s+(.*)")
description = """Python interface to OceanBase"""
with open("oceanbase_py/__init__.py", "rb") as f:
    python_client_version = _version_re.search(f.read().decode("utf-8"))
    assert python_client_version is not None
    version = str(ast.literal_eval(python_client_version.group(1)))

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name=package_name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2.0",
    author="yuanoOo",
    author_email="yuanoOo@gmail.com",
    url="https://www.oceanbase.com/",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Database :: Front-Ends",
    ],
    install_requires=[
        "sqlalchemy>=1.4, <2",
        "sqlalchemy-utils>=0.38.3, <0.39",
        "mysqlclient>=2.1.0, <3",
    ],
    packages=find_packages(include=["oceanbase_py", "oceanbase_py.*"]),
    package_data={"": ["LICENSE", "README.md"]},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'sqlalchemy.dialects': [
            'oceanbase_py = oceanbase_py.sqlalchemy.dialect:OceanBaseDialect',
            'OceanBase = oceanbase_py.sqlalchemy.dialect:OceanBaseDialect'
        ]
    },
)
