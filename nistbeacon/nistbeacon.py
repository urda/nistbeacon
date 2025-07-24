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
from typing import Optional

import requests
from requests.exceptions import RequestException

from nistbeacon.nistbeaconvalue import NistBeaconValue


class NistBeacon:
    """
    The NistBeacon object is used to query the NIST Randomness Beacon.
    For the most part, it returns actual NistBeaconValue objects for the
    consumer to use as they please.
    """

    _NIST_API_URL = "https://beacon.nist.gov/rest/record"

    # noinspection SpellCheckingInspection
    _INIT_RECORD = NistBeaconValue(
        version="Version 1.0",
        frequency=60,
        timestamp=1378395540,
        seed_value='87F49DB997D2EED0B4FDD93BAA4CDFCA49095AF98E54B81F2C39B5C400'
                   '2EC04B8C9E31FA537E64AC35FA2F038AA80730B054CFCF371AB5584CFB'
                   '4EFD293280EE',
        previous_output_value="00000000000000000000000000000000000000000000000"
                              "00000000000000000000000000000000000000000000000"
                              "0000000000000000000000000000000000",
        signature_value="F93BBE5714944F31983AE8187D5D94F87FFEC2F98185F9EB4FE5D"
                        "B61A9E5119FB0756E9AF4B7112DEBF541E9E53D05346B7358C12F"
                        "A43A8E0D695BFFAF193B1C3FFC4AE7BCF6651812B6D60190DB8FF"
                        "23C9364374737F45F1A89F22E1E492B0F373E4DB523274E9D31C8"
                        "6987C64A26F507008828A358B0E166A197D433597480895E9298C"
                        "60D079673879C3C1AEDA6306C3201991D0A6778B21462BDEBB8D3"
                        "776CD3D0FA0325AFE99B2D88A7C357E62170320EFB51F9749B5C7"
                        "B9E7347178AB051BDD097B226664A2D64AF1557BB31540601849F"
                        "0BE3AAF31D7A25E2B358EEF5A346937ADE34A110722DA8C037F97"
                        "3350B3846DCAB16C9AA125F2027C246FDB3",
        output_value="17070B49DBF3BA12BEA427CB6651ECF7860FDC3792268031B77711D6"
                     "3A8610F4CDA551B7FB331103889A62E2CB23C0F85362BBA49B9E0086"
                     "D1DA0830E4389AB1",
        status_code="1",
    )

    @classmethod
    def _query_nist(cls, url_data: str) -> Optional[NistBeaconValue]:
        try:
            nist_response = requests.get(
                url=f'{cls._NIST_API_URL}/{url_data}',
                timeout=30,
            )

            if (
                    isinstance(nist_response, requests.Response) and
                    nist_response.status_code is requests.codes.OK
            ):
                return NistBeaconValue.from_xml(nist_response.text)

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
                prev_record is None and
                isinstance(next_record, NistBeaconValue)
        ):
            # Edge case, this was potentially the first record of all time
            return (
                record.valid_signature and
                next_record.valid_signature and
                cls._INIT_RECORD == record and
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

    @classmethod
    def get_first_record(
            cls,
            download: bool=True
    ) -> NistBeaconValue:
        """
        Get the first (oldest) record available. Since the first record
        IS a known value in the system we can load it from constants.

        :param download: 'True' will always reach out to NIST to get the
                         first record. 'False' returns a local copy.
        :return: The first beacon value. 'None' otherwise.
        """

        if download:
            return NistBeacon.get_record(cls._INIT_RECORD.timestamp)

        return NistBeaconValue.from_json(cls._INIT_RECORD.json)

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

        return cls._query_nist(f'next/{timestamp}')

    @classmethod
    def get_previous(cls, timestamp: int) -> NistBeaconValue:
        """
        Given a record timestamp, get the previous record available.

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The previous beacon value if available. 'None; otherwise
        """

        return cls._query_nist(f'previous/{timestamp}')

    @classmethod
    def get_record(cls, timestamp: int) -> NistBeaconValue:
        """
        Get a specific record (or next closest)

        :param timestamp: UNIX time / POSIX time / Epoch time
        :return: The requested beacon value if available. 'None' otherwise.
        """

        return cls._query_nist(str(timestamp))
