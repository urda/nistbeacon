"""
Copyright 2015-2017 Peter Urda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from distutils.core import setup

setup(
    name='nistbeacon',
    packages=['nistbeacon'],
    version='0.9.4',

    description='Python 3 Library to access the NIST Randomness Beacon',
    long_description=open('README.rst').read(),
    license='Apache License, Version 2.0',

    author='Peter Urda',
    author_email='noreply@urda.cc',
    url='https://github.com/urda/nistbeacon',

    install_requires=[
        'pycryptodome>=2.18.4',
        'requests>=2.8.1',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ],
)
