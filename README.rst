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

Beacon Value
============

The :code:`NistRandomnessBeaconValue` objects act as basic python objects.
As one would expect, there are a number of properties and methods available
on it.

Beacon Value Properties
-----------------------

.. code:: python

    """
    :param version:
        Reported NIST randomness beacon version

    :param frequency:
        The time interval, in seconds, between expected records

    :param timestamp:
        The time the seed value was generated as the number of
        seconds since January 1, 1970

    :param seed_value:
        A seed value represented as a 64 byte (512-bit) hex string
        value

    :param previous_output_value:
        The SHA-512 hash value for the previous record - 64 byte hex
        string

    :param signature_value:
        A digital signature (RSA) computed over (in order): version,
        frequency, timeStamp, seedValue, previousHashValue, statusCode

        Note: Except for version, the hash is on the byte
        representations and not the string representations of the data
        values

    :param output_value:
        The SHA-512 hash of the signatureValue as a 64 byte hex string

    :param status_code:
        The status code value:
            0 - Chain intact, values all good
            1 - Start of a new chain of values, previous hash value
                will be all zeroes
            2 - Time between values is greater than the frequency, but
                the chain is still intact
    """

Beacon Value Methods
--------------------

.. code:: python

    @classmethod
    def from_json(cls, input_json: str):
        """
        Convert a string of JSON which represents a NIST randomness beacon
        value into a 'NistRandomnessBeaconValue' object.

        :param input_json: JSON to build a 'Nist RandomnessBeaconValue' from
        :return: A 'NistRandomnessBeaconValue' object, 'None' otherwise
        """

.. code:: python

    def to_json(self) -> str:
        """
        Convert the given NIST randomness beacon value to JSON

        :return: The JSON representation of the beacon, as a string
        """

.. code:: python

    @classmethod
    def from_xml(cls, input_xml: str):
        """
        Convert a string of XML which represents a NIST Randomness Beacon value
        into a 'NistRandomnessBeaconValue' object.

        :param input_xml: XML to build a 'NistRandomnessBeaconValue' from
        :return: A 'NistRandomnessBeaconValue' object, 'None' otherwise
        """

.. code:: python

    def to_xml(self) -> str:
        """
        Convert the given NIST randomness beacon value back to XML

        :return: The XML representation of the beacon, as a string
        """

References
==========

-  `NIST Randomness Beacon Homepage`_
-  `NIST Beacon REST API`_

.. _NIST Randomness Beacon Homepage: https://beacon.nist.gov/home
.. _NIST Beacon REST API: https://beacon.nist.gov/record/0.1/beacon-0.1.0.xsd

.. |Build Status| image:: https://travis-ci.org/urda/py_nist_beacon.svg?branch=master
   :target: https://travis-ci.org/urda/py_nist_beacon
.. |Coverage Status| image:: https://coveralls.io/repos/urda/py_nist_beacon/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/urda/py_nist_beacon?branch=master
