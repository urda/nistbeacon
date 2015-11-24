from unittest import TestCase
from unittest.mock import (
    Mock,
    patch,
)

import requests.exceptions

from py_nist_beacon import NistRandomnessBeacon
from py_nist_beacon.nist_randomness_beacon_value import (
    NistRandomnessBeaconValue
)


class TestNistRandomnessBeacon(TestCase):
    def test_get_last_record(self):
        last_record = NistRandomnessBeacon.get_last_record()

        self.assertIsInstance(last_record, NistRandomnessBeaconValue)

    def test_get_last_record_404(self):
        with patch('requests.get') as patched_requests:
            mock_response = Mock()
            mock_response.status_code = 404
            patched_requests.return_value = mock_response

            self.assertIsNone(NistRandomnessBeacon.get_last_record())

    def test_get_last_record_exceptions(self):
        exceptions_to_test = [
            requests.exceptions.RequestException(),
            requests.exceptions.ConnectionError(),
            requests.exceptions.HTTPError(),
            requests.exceptions.URLRequired(),
            requests.exceptions.TooManyRedirects(),
            requests.exceptions.Timeout(),
        ]

        for exception_to_test in exceptions_to_test:
            with patch('requests.get') as patched_requests:
                patched_requests.side_effect = exception_to_test
                self.assertIsNone(NistRandomnessBeacon.get_last_record())
