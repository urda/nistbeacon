Beacon Usage
============

It is easy to use the beacon. Most queries are performed through
:code:`NistBeacon` which produces :code:`NistBeaconValue` objects.

Sample Code
-----------

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

:code:`chain_check`
^^^^^^^^^^^^^^^^^^^

.. code:: python

    @classmethod
    def chain_check(cls, timestamp: int) -> bool:
        """
        Given a record timestamp, verify the chain integrity.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: 'True' if the timestamp fits the chain. 'False' otherwise.
        """

:code:`get_first_record`
^^^^^^^^^^^^^^^^^^^^^^^^

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

:code:`get_last_record`
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    @classmethod
    def get_last_record(cls) -> NistBeaconValue:
        """
        Get the last (newest) record available.

        :return: The last beacon value. 'None' otherwise.
        """

:code:`get_next`
^^^^^^^^^^^^^^^^

.. code:: python

    @classmethod
    def get_next(cls, timestamp: int) -> NistBeaconValue:
        """
        Given a record timestamp, get the next record available.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The next beacon value if available. 'None' otherwise.
        """

:code:`get_previous`
^^^^^^^^^^^^^^^^^^^^

.. code:: python

    @classmethod
    def get_previous(cls, timestamp: int) -> NistBeaconValue:
        """
        Given a record timestamp, get the previous record available.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The previous beacon value if available. 'None; otherwise
        """

:code:`get_record`
^^^^^^^^^^^^^^^^^^

.. code:: python

    @classmethod
    def get_record(cls, timestamp: int) -> NistBeaconValue:
        """
        Get a specific record (or next closest)

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The requested beacon value if available. 'None' otherwise.
        """
