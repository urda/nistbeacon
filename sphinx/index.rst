.. NistBeacon documentation master file, created by
   sphinx-quickstart on Sat Sep 16 17:08:24 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NistBeacon: NIST randomness beacon with python
==============================================

.. image:: https://travis-ci.org/urda/nistbeacon.svg?branch=master
    :target: https://travis-ci.org/urda/nistbeacon

.. image:: https://codecov.io/gh/urda/nistbeacon/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/urda/nistbeacon/branch/master

.. image:: https://img.shields.io/pypi/l/nistbeacon.svg
    :target: https://pypi.python.org/pypi/nistbeacon

.. image:: https://img.shields.io/pypi/pyversions/nistbeacon.svg
    :target: https://pypi.python.org/pypi/nistbeacon

Important Notice!
=================

**WARNING: DO NOT USE BEACON GENERATED VALUES AS SECRET CRYPTOGRAPHIC KEYS.**

Remember, these random numbers are not only available over the public internet,
but are kept on "record" and can be accessed at anytime with just a timestamp.
Make sure you understand the implications of using the NIST randomness beacon
in your projects.

Contents
========

.. toctree::
    :maxdepth: 2

    installation
    usage
    beacon_values
    project_information
    changelog

.. Indices and tables
   ==================
   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
