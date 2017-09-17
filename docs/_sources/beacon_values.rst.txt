Beacon Value
============

The :code:`NistBeaconValue` objects act as basic python objects.
As one would expect, there are a number of properties and methods available
on it.

Instance Details
----------------

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

Properties
----------

:code:`frequency`
^^^^^^^^^^^^^^^^^

.. code:: python

    @property
    def frequency(self) -> int:
        """
        :return: The time interval, in seconds, between expected records
        """

:code:`json`
^^^^^^^^^^^^

.. code:: python

    @property
    def json(self) -> str:
        """
        :return: The JSON representation of the beacon, as a string
        """

:code:`output_value`
^^^^^^^^^^^^^^^^^^^^

.. code:: python

    @property
    def output_value(self) -> str:
        """
        :return: The SHA-512 hash of the signatureValue as a 64 byte hex string
        """

:code:`previous_output_value`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    @property
    def previous_output_value(self) -> str:
        """
        :return:
            The SHA-512 hash value for the previous record - 64 byte hex
            string
        """

:code:`pseudo_random`
^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    @property
    def pseudo_random(self) -> Random:
        """
        :return:
            A python `random.Random` object that has been seeded with
            the value's `output_value`. This is a pseudo-random
            number generator
        """

:code:`seed_value`
^^^^^^^^^^^^^^^^^^

.. code:: python

    @property
    def seed_value(self) -> str:
        """
        :return:
            A seed value represented as a 64 byte (512-bit) hex string
            value
        """

:code:`signature_value`
^^^^^^^^^^^^^^^^^^^^^^^

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

:code:`status_code`
^^^^^^^^^^^^^^^^^^^

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

:code:`timestamp`
^^^^^^^^^^^^^^^^^

.. code:: python

    @property
    def timestamp(self) -> int:
        """
        :return:
            The time the seed value was generated as the number of
            seconds since January 1, 1970
        """

:code:`valid_signature`
^^^^^^^^^^^^^^^^^^^^^^^

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

:code:`version`
^^^^^^^^^^^^^^^

.. code:: python

    @property
    def version(self) -> str:
        """
        :return: Reported NIST randomness beacon version
        """

:code:`xml`
^^^^^^^^^^^

.. code:: python

    @property
    def xml(self) -> str:
        """
        :return: The XML representation of the beacon, as a string
        """

Methods
-------

:code:`from_json`
^^^^^^^^^^^^^^^^^

.. code:: python

    @classmethod
    def from_json(cls, input_json: str):
        """
        Convert a string of JSON which represents a NIST randomness beacon
        value into a 'NistBeaconValue' object.

        :param input_json: JSON to build a 'Nist RandomnessBeaconValue' from
        :return: A 'NistBeaconValue' object, 'None' otherwise
        """

:code:`from_xml`
^^^^^^^^^^^^^^^^

.. code:: python

    @classmethod
    def from_xml(cls, input_xml: str):
        """
        Convert a string of XML which represents a NIST Randomness Beacon value
        into a 'NistBeaconValue' object.

        :param input_xml: XML to build a 'NistBeaconValue' from
        :return: A 'NistBeaconValue' object, 'None' otherwise
