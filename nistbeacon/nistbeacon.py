"""
Copyright 2015 Peter Urda

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

import requests
from requests.exceptions import RequestException

import nistbeacon.constants as cn
from nistbeacon.nistbeaconvalue import NistBeaconValue


class NistBeacon(object):
    """
    The NistBeacon object is used to query the NIST Randomness Beacon.
    For the most part, it returns actual NistBeaconValue objects for the
    consumer to use as they please.
    """

    _NIST_API_URL = "https://beacon.nist.gov/rest/record"

    @classmethod
    def _query_nist(cls, url_data: str) -> NistBeaconValue:
        try:
            nist_response = requests.get(
                "{0}/{1}".format(
                    cls._NIST_API_URL,
                    url_data,
                )
            )

            if (
                    isinstance(nist_response, requests.Response) and
                    nist_response.status_code is requests.codes.OK
            ):
                return NistBeaconValue.from_xml(nist_response.text)
            else:
                return None
        except RequestException:
            return None

    @classmethod
    def chain_check(cls, timestamp: int) -> bool:
        """
        Given a record timestamp, verify the chain integrity.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: 'True' if the timestamp fits the chain. 'False' otherwise.
        """

        # Creation is messy.
        # You want genius, you get madness; two sides of the same coin.
        # ... I'm sure this can be cleaned up. However, let's test it first.

        record = cls.get_record(timestamp)

        if isinstance(record, NistBeaconValue) is False:
            # Don't you dare try to play me
            return False

        prev_record = cls.get_previous(record.timestamp)
        next_record = cls.get_next(record.timestamp)

        if prev_record is None and next_record is None:
            # Uh, how did you manage to do this?
            # I'm not even mad, that's amazing.
            return False

        if (
                isinstance(prev_record, NistBeaconValue) and
                isinstance(next_record, NistBeaconValue)
        ):
            # Majority case, somewhere in the middle of the chain
            # True if:
            #   - All three records have proper signatures
            #   - The requested record's previous output equals previous
            #   - The next possible record's previous output equals the record
            return (
                record.valid_signature and
                prev_record.valid_signature and
                next_record.valid_signature and
                record.previous_output_value == prev_record.output_value and
                next_record.previous_output_value == record.output_value
            )

        if (
                prev_record is None and
                isinstance(next_record, NistBeaconValue)
        ):
            # Edge case, this was potentially the first record of all time
            init_ref = NistBeaconValue.from_json(
                cn.NIST_INIT_RECORD,
            )

            return (
                record.valid_signature and
                next_record.valid_signature and
                init_ref == record and
                next_record.previous_output_value == record.output_value
            )

        if (
                isinstance(prev_record, NistBeaconValue) and
                next_record is None
        ):
            # Edge case, this was potentially the latest and greatest
            return (
                record.valid_signature and
                prev_record.valid_signature and
                record.previous_output_value == prev_record.output_value
            )

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

        if download:
            return NistBeacon.get_record(
                cn.NIST_INIT_RECORD_TIMESTAMP
            )
        else:
            return NistBeaconValue.from_json(cn.NIST_INIT_RECORD)

    @classmethod
    def get_last_record(cls) -> NistBeaconValue:
        """
        Get the last (newest) record available.

        :return: The last beacon value. 'None' otherwise.
        """

        return cls._query_nist("last")

    @classmethod
    def get_next(cls, timestamp: int) -> NistBeaconValue:
        """
        Given a record timestamp, get the next record available.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The next beacon value if available. 'None' otherwise.
        """

        return cls._query_nist("next/{}".format(timestamp))

    @classmethod
    def get_previous(cls, timestamp: int) -> NistBeaconValue:
        """
        Given a record timestamp, get the previous record available.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The previous beacon value if available. 'None; otherwise
        """

        return cls._query_nist("previous/{}".format(timestamp))

    @classmethod
    def get_record(cls, timestamp: int) -> NistBeaconValue:
        """
        Get a specific record (or next closest)

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The requested beacon value if available. 'None' otherwise.
        """

        return cls._query_nist(str(timestamp))
