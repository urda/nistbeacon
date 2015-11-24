import requests
from requests.exceptions import RequestException

from py_nist_beacon.nist_randomness_beacon_value import (
    NistRandomnessBeaconValue
)


class NistRandomnessBeacon(object):
    NIST_BASE_URL = "https://beacon.nist.gov/rest/record"

    @classmethod
    def get_last_record(cls):
        try:
            r = requests.get("{}/last".format(cls.NIST_BASE_URL))

            if r.status_code is requests.codes.OK:
                return NistRandomnessBeaconValue.from_xml(r.text)
            else:
                return None
        except RequestException:
            return None

    @classmethod
    def get_next(cls, timestamp: int):
        try:
            r = requests.get(
                "{0}/next/{1}".format(
                    cls.NIST_BASE_URL,
                    timestamp,
                )
            )

            if r.status_code is requests.codes.OK:
                return NistRandomnessBeaconValue.from_xml(r.text)
            else:
                return None
        except RequestException:
            return None

    @classmethod
    def get_previous(cls, timestamp: int):
        try:
            r = requests.get(
                "{0}/previous/{1}".format(
                    cls.NIST_BASE_URL,
                    timestamp,
                )
            )

            if r.status_code is requests.codes.OK:
                return NistRandomnessBeaconValue.from_xml(r.text)
            else:
                return None
        except RequestException:
            return None

    @classmethod
    def get_record(cls, timestamp: int):
        try:
            r = requests.get(
                "{0}/{1}".format(
                    cls.NIST_BASE_URL,
                    timestamp,
                )
            )

            if r.status_code is requests.codes.OK:
                return NistRandomnessBeaconValue.from_xml(r.text)
            else:
                return None
        except RequestException:
            return None
