Python NIST Randomness Beacon
=============================

**WARNING: DO NOT USE BEACON GENERATED VALUES AS SECRET CRYPTOGRAPHIC
KEYS.**

Installation
============

Prerequisites
-------------

A required library :code:`pycrypto` is used with :code:`nistbeacon`.

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

Beacon Methods
--------------

.. code:: python

    @classmethod
    def chain_check(cls, timestamp: int) -> bool:
        """
        Given a record timestamp, verify the chain integrity.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: 'True' if the timestamp fits the chain. 'False' otherwise.
        """

.. code:: python

    @classmethod
    def get_first_record(
            cls,
            download: bool=False
    ) -> NistBeaconValue:
        """
        Get the first (oldest) record available. Since the first record
        IS a known value in the system we can load it from constants.

        :param download: 'True' will always reach out to NIST to get the
                         first record. 'False' returns a local copy.
        :return: The first beacon value. 'None' otherwise.
        """

.. code:: python

    @classmethod
    def get_last_record(cls) -> NistBeaconValue:
        """
        Get the last (newest) record available.

        :return: The last beacon value. 'None' otherwise.
        """

.. code:: python

    @classmethod
    def get_next(cls, timestamp: int) -> NistBeaconValue:
        """
        Given a record timestamp, get the next record available.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The next beacon value if available. 'None' otherwise.
        """

.. code:: python

    @classmethod
    def get_previous(cls, timestamp: int) -> NistBeaconValue:
        """
        Given a record timestamp, get the previous record available.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The previous beacon value if available. 'None; otherwise
        """

.. code:: python

    @classmethod
    def get_record(cls, timestamp: int) -> NistBeaconValue:
        """
        Get a specific record (or next closest)

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The requested beacon value if available. 'None' otherwise.
        """

Beacon Value
============

The :code:`NistBeaconValue` objects act as basic python objects.
As one would expect, there are a number of properties and methods available
on it.

Beacon Value Instance
---------------------

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

Beacon Value Properties
-----------------------

.. code:: python

    @property
    def frequency(self) -> int:
        """
        :return: The time interval, in seconds, between expected records
        """

.. code:: python

    @property
    def json(self) -> str:
        """
        :return: The JSON representation of the beacon, as a string
        """

.. code:: python

    @property
    def output_value(self) -> str:
        """
        :return: The SHA-512 hash of the signatureValue as a 64 byte hex string
        """

.. code:: python

    @property
    def previous_output_value(self) -> str:
        """
        :return:
            The SHA-512 hash value for the previous record - 64 byte hex
            string
        """

.. code:: python

    @property
    def pseudo_random(self) -> Random:
        """
        :return:
            A python `random.Random` object that has been seeded with
            the value's `output_value`. This is a pseudo-random
            number generator
        """

.. code:: python

    @property
    def seed_value(self) -> str:
        """
        :return:
            A seed value represented as a 64 byte (512-bit) hex string
            value
        """

.. code:: python

    @property
    def signature_value(self) -> str:
        """
        :return:
            A digital signature (RSA) computed over (in order): version,
            frequency, timeStamp, seedValue, previousHashValue, statusCode

            Note: Except for version, the hash is on the byte
            representations and not the string representations of the data
            values
        """

.. code:: python

    @property
    def status_code(self) -> str:
        """
        :return:
            The status code value:
                0 - Chain intact, values all good
                1 - Start of a new chain of values, previous hash value
                    will be all zeroes
                2 - Time between values is greater than the frequency, but
                    the chain is still intact
        """

.. code:: python

    @property
    def timestamp(self) -> int:
        """
        :return:
            The time the seed value was generated as the number of
            seconds since January 1, 1970
        """

.. code:: python

    @property
    def valid_signature(self) -> bool:
        """
        Shows the result of signature verification

        First, required records (version, frequency, timestamp,
        seed_value, previous_output_value) are packed together to form
        a message. This message is then checked against the record's reported
        signature field WITH the known NIST public key.

        Second, the signature value is independently ran through a SHA512
        hash. The result of this operation SHOULD equal the record's reported
        output_value field.

        As long as the result of the 'First' step and'ed with the 'Second'
        step, the record is considered valid.

        :return: 'True' if this record is valid. 'False' otherwise
        """

.. code:: python

    @property
    def version(self) -> str:
        """
        :return: Reported NIST randomness beacon version
        """

.. code:: python

    @property
    def xml(self) -> str:
        """
        :return: The XML representation of the beacon, as a string
        """

Beacon Value Methods
--------------------

.. code:: python

    @classmethod
    def from_json(cls, input_json: str):
        """
        Convert a string of JSON which represents a NIST randomness beacon
        value into a 'NistBeaconValue' object.

        :param input_json: JSON to build a 'Nist RandomnessBeaconValue' from
        :return: A 'NistBeaconValue' object, 'None' otherwise
        """

.. code:: python

    @classmethod
    def from_xml(cls, input_xml: str):
        """
        Convert a string of XML which represents a NIST Randomness Beacon value
        into a 'NistBeaconValue' object.

        :param input_xml: XML to build a 'NistBeaconValue' from
        :return: A 'NistBeaconValue' object, 'None' otherwise
        """

Contributing
============

Please refer to the
`CONTRIBUTING <https://github.com/urda/nistbeacon/blob/master/CONTRIBUTING.md>`_
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
