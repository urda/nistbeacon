import requests
from requests.exceptions import RequestException

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
