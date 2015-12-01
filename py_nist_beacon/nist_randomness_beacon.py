import requests
from requests.exceptions import RequestException

import py_nist_beacon.nist_beacon_constants as cn
from py_nist_beacon.nist_randomness_beacon_value import (
    NistRandomnessBeaconValue
)


class NistRandomnessBeacon(object):
    NIST_BASE_URL = "https://beacon.nist.gov/rest/record"

    @classmethod
    def _query_nist(cls, url_data: str) -> NistRandomnessBeaconValue:
        try:
            r = requests.get(
                "{0}/{1}".format(
                    cls.NIST_BASE_URL,
                    url_data,
                )
            )

            if r.status_code is requests.codes.OK:
                return NistRandomnessBeaconValue.from_xml(r.text)
            else:
                return None
        except RequestException:
            return None

    @classmethod
    def chain_check(cls, record: NistRandomnessBeaconValue) -> bool:
        # Creation is messy.
        # You want genius, you get madness; two sides of the same coin.

        # Lots of things to check ...
        #
        # prev_record.output_value == record.previous_output_value
        # record.output_value == next_record.previous_output_value
        #
        # Verify all signatures
        # Most cases? Will have a next and prev
        # Edge cases?
        #
        # IF it's the FIRST record of all time (1378395540)
        # ... then things happen differently
        # IF It's the LATEST record
        # ... you guessed it, things happen differently

        if isinstance(record, NistRandomnessBeaconValue) is False:
            # Don't you dare try to play me
            return False

        prev_record = cls.get_previous(record.timestamp)
        next_record = cls.get_next(record.timestamp)

        if prev_record is None and next_record is None:
            # Uh, how did you manage to do this?
            # I'm not even mad, that's amazing.
            return False

        if (
            isinstance(prev_record, NistRandomnessBeaconValue) and
            isinstance(next_record, NistRandomnessBeaconValue)
        ):
            # Majority case, somewhere in the middle of the chain
            return False

        if (
            isinstance(prev_record, NistRandomnessBeaconValue) and
            next_record is None
        ):
            # Edge case, this was potentially the latest and greatest
            return False

        if (
            prev_record is None and
            isinstance(next_record, NistRandomnessBeaconValue)
        ):
            # Edge case, this was potentially the first record of all time
            init_ref = NistRandomnessBeaconValue.from_json(
                cn.NIST_INIT_RECORD,
            )

            return False

    @classmethod
    def get_last_record(cls) -> NistRandomnessBeaconValue:
        return cls._query_nist("last")

    @classmethod
    def get_next(cls, timestamp: int) -> NistRandomnessBeaconValue:
        return cls._query_nist("next/{}".format(timestamp))

    @classmethod
    def get_previous(cls, timestamp: int) -> NistRandomnessBeaconValue:
        return cls._query_nist("previous/{}".format(timestamp))

    @classmethod
    def get_record(cls, timestamp: int) -> NistRandomnessBeaconValue:
        return cls._query_nist(str(timestamp))
