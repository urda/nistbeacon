from distutils.core import setup

setup(
    name='py_nist_beacon',
    packages=['py_nist_beacon'],
    version='0.5.0',

    description='Python 3 Library to access the NIST Randomness Beacon',
    long_description=open('README.rst').read(),
    license='Apache License, Version 2.0',

    author='Peter Urda',
    author_email='noreply@urda.cc',
    url='https://github.com/urda/py_nist_beacon',

    install_requires=[
        'pycrypto>=2.6.1',
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
