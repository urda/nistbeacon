|Build Status| |Coverage Status|

Python NIST Randomness Beacon
=============================

**WARNING: DO NOT USE BEACON GENERATED VALUES AS SECRET CRYPTOGRAPHIC
KEYS.**

Usage
=====

Start by importing the beacon into your project:

.. code:: python

    from py_nist_beacon import NistRandomnessBeacon

Then simply use the various methods on the beacon to get values back
out:

.. code:: python

    # In the examples below I will be using 1447873020 as my <timestamp> when required

    # Current Record (or next closest) - https://beacon.nist.gov/rest/record/<timestamp>
    record = NistRandomnessBeacon.get_record(1447873020)

    # Previous Record - https://beacon.nist.gov/rest/record/previous/<timestamp>
    record = NistRandomnessBeacon.get_previous(1447873020)

    # Next Record - https://beacon.nist.gov/rest/record/next/<timestamp>
    record = NistRandomnessBeacon.get_next(1447873020)

    # Last Record - https://beacon.nist.gov/rest/record/last
    record = NistRandomnessBeacon.get_last_record()

References
----------

-  `NIST Randomness Beacon Homepage`_
-  `NIST Beacon REST API`_

.. _NIST Randomness Beacon Homepage: https://beacon.nist.gov/home
.. _NIST Beacon REST API: https://beacon.nist.gov/record/0.1/beacon-0.1.0.xsd

.. |Build Status| image:: https://travis-ci.org/urda/py_nist_beacon.svg?branch=master
   :target: https://travis-ci.org/urda/py_nist_beacon
.. |Coverage Status| image:: https://coveralls.io/repos/urda/py_nist_beacon/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/urda/py_nist_beacon?branch=master
