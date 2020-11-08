"""
Copyright 2015-2020 Peter Urda

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

from setuptools import setup

setup(
    name='nistbeacon',
    version='0.9.4',
    python_requires=">=3.6, <4",
    packages=['nistbeacon'],
    include_package_data=True,
    license='Apache License, Version 2.0',

    description='Python 3 Library to access the NIST Randomness Beacon',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='https://github.com/urda/nistbeacon',

    author='Peter Urda',
    author_email='noreply@urda.com',

    install_requires=[
        'pycryptodome>=3.4.7,<4',
        'requests>=2.18.4,<3',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Utilities',
    ],
)
