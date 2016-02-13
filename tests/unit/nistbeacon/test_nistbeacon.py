from unittest import TestCase
from unittest.mock import (
    Mock,
    patch,
)

import requests.exceptions
from requests import Response

import nistbeacon.constants as cn
from nistbeacon import (
    NistBeacon,
    NistBeaconValue,
)
from tests.test_data.nist_records import local_record_db


class TestNistBeacon(TestCase):
    @classmethod
    def setUpClass(cls):
        init_timestamp = 1378395540
        cls.expected_first = local_record_db[init_timestamp]
        cls.expected_first_next = local_record_db[init_timestamp + 60]

        cls.reference_timestamp = int(1447873020)
        cls.expected_current = local_record_db[cls.reference_timestamp]
        cls.expected_next = local_record_db[cls.reference_timestamp + 60]
        cls.expected_previous = local_record_db[cls.reference_timestamp - 60]

    def test_get_first_record(self):
        expected = NistBeacon.get_first_record(download=False)

        with patch('requests.get') as requests_patch:
            # Configure mocked Response object
            record = NistBeaconValue.from_json(cn.NIST_INIT_RECORD)

            mock_response = Mock(spec=Response)
            mock_response.status_code = 200
            mock_response.text = record.xml

            requests_patch.side_effect = [
                mock_response,
                mock_response,
            ]

            downloaded = NistBeacon.get_first_record(download=True)
            actual = NistBeacon.get_record(cn.NIST_INIT_RECORD_TIMESTAMP)

        download_error_msg = (
            "Failed to confirm the first record! "
            "Check the remote NIST service."
        )

        same_object_error_msg = (
            "These should have been two unique objects regardless of equality."
        )

        self.assertEqual(
            expected,
            actual,
            msg=download_error_msg,
        )

        self.assertEqual(
            expected,
            downloaded,
            msg=download_error_msg,
        )

        test_pairs = [
            (expected, actual),
            (expected, downloaded),
            (actual, downloaded),
        ]

        for pair in test_pairs:
            self.assertIsNot(
                pair[0],
                pair[1],
                msg=same_object_error_msg,
            )

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
        # Configure mocked Response object
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
        # Configure mocked Response object
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.text = self.expected_current.xml
        requests_get_patched.return_value = mock_response

        # Get the record (which will actually be the Mocked response)
        record = NistBeacon.get_record(self.reference_timestamp)
        self.assertEqual(self.expected_current, record)

    @patch('requests.get')
    def test_get_last_record(self, requests_get_patched):
        # Configure mocked Response object
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200
        mock_response.text = self.expected_current.xml
        requests_get_patched.return_value = mock_response

        # Get the "last" record. But this will just return a generic record
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

    def test_chain_check_empty_input(self):
        # noinspection PyTypeChecker
        self.assertFalse(NistBeacon.chain_check(None))

    @patch('nistbeacon.NistBeacon.get_record')
    @patch('nistbeacon.NistBeacon.get_next')
    @patch('nistbeacon.NistBeacon.get_previous')
    def test_chain_check_majority(self, prev_call, next_call, get_call):
        prev_call.return_value = self.expected_previous
        next_call.return_value = self.expected_next
        get_call.return_value = self.expected_current

        self.assertTrue(
            NistBeacon.chain_check(
                self.expected_current.timestamp
            )
        )

    @patch('nistbeacon.NistBeacon.get_record')
    @patch('nistbeacon.NistBeacon.get_next')
    @patch('nistbeacon.NistBeacon.get_previous')
    def test_chain_check_init(self, prev_call, next_call, get_call):
        prev_call.return_value = None
        next_call.return_value = self.expected_first_next
        get_call.return_value = NistBeacon.get_first_record(download=False)

        self.assertTrue(
            NistBeacon.chain_check(
                cn.NIST_INIT_RECORD_TIMESTAMP,
            )
        )

    @patch('nistbeacon.NistBeacon.get_record')
    @patch('nistbeacon.NistBeacon.get_next')
    @patch('nistbeacon.NistBeacon.get_previous')
    def test_chain_check_last(self, prev_call, next_call, get_call):
        prev_call.return_value = self.expected_previous
        next_call.return_value = None
        get_call.return_value = self.expected_current

        self.assertTrue(
            NistBeacon.chain_check(
                self.expected_current.timestamp,
            )
        )

    @patch('nistbeacon.NistBeacon.get_next')
    @patch('nistbeacon.NistBeacon.get_previous')
    def test_chain_check_no_records_around(self, prev_call, next_call):
        prev_call.return_value = None
        next_call.return_value = None
        self.assertFalse(
            NistBeacon.chain_check(
                self.expected_current.timestamp
            )
        )
