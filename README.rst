Python NIST Randomness Beacon
=============================

**WARNING: DO NOT USE BEACON GENERATED VALUES AS SECRET CRYPTOGRAPHIC
KEYS.**

Installation
============

Prerequisites
-------------

A required library :code:`pycryptodome` is used with :code:`nistbeacon`.

Ubuntu, and other Linux-based users should have :code:`python3-dev` installed.

.. code:: bash

    apt-get install python3-dev

Installing :code:`nistbeacon`
-----------------------------

To install the beacon library, simply use :code:`pip`:

.. code:: bash

    pip install nistbeacon

Beacon Usage
============

It is easy to use the beacon. Most queries are performed through
:code:`NistBeacon` which produces :code:`NistBeaconValue` objects.

Beacon Sample Code
------------------

.. code:: python

    from nistbeacon import NistBeacon

    # In the examples below I will be using 1447873020
    # as my <timestamp> when required

    # Current Record (or next closest)
    # https://beacon.nist.gov/rest/record/<timestamp>
    record = NistBeacon.get_record(1447873020)

    # Previous Record
    # https://beacon.nist.gov/rest/record/previous/<timestamp>
    prev_record = NistBeacon.get_previous(1447873020)

    # Next Record
    # https://beacon.nist.gov/rest/record/next/<timestamp>
    next_record = NistBeacon.get_next(1447873020)

    # First Record
    # https://beacon.nist.gov/rest/record/1378395540
    first_record = NistBeacon.get_first_record(download=True)

    # Last Record
    # https://beacon.nist.gov/rest/record/last
    last_record = NistBeacon.get_last_record()

    # Verify the record and the record chain
    record_chain_result = NistBeacon.chain_check(1447873020)

Further Documentation
=====================

Please refer to the
`official documentation <https://urda.github.io/nistbeacon/>`_
to dive deeper into :code:`NistBeacon` and :code:`NistBeaconValue` objects.

Contributing
============

Please refer to the
`CONTRIBUTING <https://github.com/urda/nistbeacon/blob/master/.github/CONTRIBUTING.md>`_
document on GitHub

Project Health
==============

+---------+-----------------+--------------------+
| Branch  | Build Status    | Coverage Status    |
+=========+=================+====================+
| Master  | |MasterBuild|_  | |MasterCoverage|_  |
+---------+-----------------+--------------------+
| Develop | |DevelopBuild|_ | |DevelopCoverage|_ |
+---------+-----------------+--------------------+

References
==========

-  `NIST Randomness Beacon Homepage <https://beacon.nist.gov/home>`_
-  `NIST Beacon REST API <https://beacon.nist.gov/record/0.1/beacon-0.1.0.xsd>`_

.. |MasterBuild| image:: https://travis-ci.org/urda/nistbeacon.svg?branch=master
.. _MasterBuild: https://travis-ci.org/urda/nistbeacon
.. |MasterCoverage| image::  https://codecov.io/gh/urda/nistbeacon/branch/master/graph/badge.svg
.. _MasterCoverage: https://codecov.io/gh/urda/nistbeacon/branch/master

.. |DevelopBuild| image:: https://travis-ci.org/urda/nistbeacon.svg?branch=develop
.. _DevelopBuild: https://travis-ci.org/urda/nistbeacon
.. |DevelopCoverage| image:: https://codecov.io/gh/urda/nistbeacon/branch/develop/graph/badge.svg
.. _DevelopCoverage: https://codecov.io/gh/urda/nistbeacon/branch/develop
