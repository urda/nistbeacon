"""
Copyright 2015-2017 Peter Urda

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

from unittest import TestCase
from unittest.mock import (
    Mock,
    patch,
)

import requests.exceptions
from requests import Response

from nistbeacon import (
    NistBeacon,
    NistBeaconValue,
)
from tests.test_data.nist_records import local_record_json_db


class TestNistBeacon(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.init_timestamp = 1378395540
        cls.expected_first = local_record_json_db[cls.init_timestamp]
        cls.expected_first_next = local_record_json_db[cls.init_timestamp + 60]

        cls.reference_previous = 1447872960
        cls.reference_timestamp = 1447873020
        cls.reference_next = 1447873080

        cls.expected_current = local_record_json_db[cls.reference_timestamp]
        cls.expected_next = local_record_json_db[cls.reference_next]
        cls.expected_previous = local_record_json_db[cls.reference_previous]

        # Perform conversions from json data to record objects
        cls.expected_first = NistBeaconValue.from_json(cls.expected_first)
        cls.expected_first_next = NistBeaconValue.from_json(
            cls.expected_first_next
        )

        cls.expected_current = NistBeaconValue.from_json(cls.expected_current)
        cls.expected_next = NistBeaconValue.from_json(cls.expected_next)
        cls.expected_previous = NistBeaconValue.from_json(
            cls.expected_previous
        )

    @patch('requests.get')
    def test_get_first_record(self, requests_get_patched):
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.text = self.expected_first.xml
        requests_get_patched.return_value = mock_response

        expected = self.expected_first
        actual_download_false = NistBeacon.get_first_record(download=False)
        actual_download_true = NistBeacon.get_first_record(download=True)

        self.assertEqual(expected, actual_download_false)
        self.assertEqual(expected, actual_download_true)

        self.assertIsNot(expected, actual_download_false)
        self.assertIsNot(expected, actual_download_true)
        self.assertIsNot(actual_download_false, actual_download_true)

    @patch('requests.get')
    def test_get_next(self, requests_get_patched):
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.text = self.expected_next.xml
        requests_get_patched.return_value = mock_response

        next_record = NistBeacon.get_next(self.reference_timestamp)
        self.assertEqual(self.expected_next, next_record)

    @patch('requests.get')
    def test_get_previous(self, requests_get_patched):
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.text = self.expected_previous.xml
        requests_get_patched.return_value = mock_response

        previous_record = NistBeacon.get_previous(
            self.reference_timestamp
        )
        self.assertEqual(self.expected_previous, previous_record)

    @patch('requests.get')
    def test_get_record(self, requests_get_patched):
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.text = self.expected_current.xml
        requests_get_patched.return_value = mock_response

        record = NistBeacon.get_record(self.reference_timestamp)
        self.assertEqual(self.expected_current, record)

    @patch('requests.get')
    def test_get_last_record(self, requests_get_patched):
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.text = self.expected_current.xml
        requests_get_patched.return_value = mock_response

        last_record = NistBeacon.get_last_record()
        self.assertIsInstance(last_record, NistBeaconValue)

    @patch('requests.get')
    def test_get_last_record_404(self, requests_get_patched):
        mock_response = Mock(spec=Response)
        mock_response.status_code = 404
        requests_get_patched.return_value = mock_response

        self.assertIsNone(NistBeacon.get_last_record())

    @patch('requests.get')
    def test_get_last_record_exceptions(self, requests_get_patched):
        exceptions_to_test = [
            requests.exceptions.RequestException(),
            requests.exceptions.ConnectionError(),
            requests.exceptions.HTTPError(),
            requests.exceptions.URLRequired(),
            requests.exceptions.TooManyRedirects(),
            requests.exceptions.Timeout(),
        ]

        for exception_to_test in exceptions_to_test:
            requests_get_patched.side_effect = exception_to_test
            self.assertIsNone(NistBeacon.get_last_record())

    @patch('requests.get')
    def test_chain_check_empty_input(self, requests_get_patched):
        mock_response = Mock(spec=Response)
        mock_response.status_code = 404
        requests_get_patched.return_value = mock_response

        # noinspection PyTypeChecker
        self.assertFalse(NistBeacon.chain_check(None))

    @patch('requests.get')
    def test_chain_check_majority(self, requests_get_patched):
        first_response = Mock(spec=Response)
        first_response.status_code = 200
        first_response.text = self.expected_current.xml

        previous_response = Mock(spec=Response)
        previous_response.status_code = 200
        previous_response.text = self.expected_previous.xml

        next_response = Mock(spec=Response)
        next_response.status_code = 200
        next_response.text = self.expected_next.xml

        requests_get_patched.side_effect = [
            first_response,
            previous_response,
            next_response,
        ]

        self.assertTrue(
            NistBeacon.chain_check(
                self.expected_current.timestamp
            )
        )

    @patch('requests.get')
    def test_chain_check_init(self, requests_get_patched):
        first_response = Mock(spec=Response)
        first_response.status_code = 200
        first_response.text = self.expected_first.xml

        previous_response = Mock(spec=Response)
        previous_response.status_code = 404

        next_response = Mock(spec=Response)
        next_response.status_code = 200
        next_response.text = self.expected_first_next.xml

        requests_get_patched.side_effect = [
            first_response,
            previous_response,
            next_response,
        ]

        self.assertTrue(
            NistBeacon.chain_check(
                self.init_timestamp,
            )
        )

    @patch('requests.get')
    def test_chain_check_last(self, requests_get_patched):
        first_response = Mock(spec=Response)
        first_response.status_code = 200
        first_response.text = self.expected_current.xml

        previous_response = Mock(spec=Response)
        previous_response.status_code = 200
        previous_response.text = self.expected_previous.xml

        next_response = Mock(spec=Response)
        next_response.status_code = 404

        requests_get_patched.side_effect = [
            first_response,
            previous_response,
            next_response,
        ]

        self.assertTrue(
            NistBeacon.chain_check(
                self.expected_current.timestamp,
            )
        )

    @patch('requests.get')
    def test_chain_check_no_records_around(self, requests_get_patched):
        first_response = Mock(spec=Response)
        first_response.status_code = 200
        first_response.text = self.expected_current.xml

        none_response = Mock(spec=Response)
        none_response.status_code = 404

        requests_get_patched.side_effect = [
            first_response,
            none_response,
            none_response,
        ]

        self.assertFalse(
            NistBeacon.chain_check(
                self.expected_current.timestamp
            )
        )
