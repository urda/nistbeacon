from unittest import TestCase

from nistbeacon import (
    NistBeacon,
    NistBeaconValue,
)
from tests.test_data.nist_records import local_record_db


class TestNistIntegration(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.target_timestamp = 1447873020

        cls.focus_record = local_record_db[cls.target_timestamp]
        cls.next_record = local_record_db[cls.target_timestamp + 60]
        cls.previous_record = local_record_db[cls.target_timestamp - 60]

    def test_get_last_record(self):
        actual = NistBeacon.get_last_record()

        self.assertIsInstance(actual, NistBeaconValue)
        self.assertTrue(actual.valid_signature)

    def test_get_next(self):
        expected = self.next_record
        actual = NistBeacon.get_next(self.target_timestamp)

        self.assertIsInstance(actual, NistBeaconValue)
        self.assertTrue(actual.valid_signature)
        self.assertEqual(expected, actual)
        self.assertIsNot(expected, actual)

    def test_get_previous(self):
        expected = self.previous_record
        actual = NistBeacon.get_previous(self.target_timestamp)

        self.assertIsInstance(actual, NistBeaconValue)
        self.assertTrue(actual.valid_signature)
        self.assertEqual(expected, actual)
        self.assertIsNot(expected, actual)

    def test_get_record(self):
        expected = self.focus_record
        actual = NistBeacon.get_record(self.target_timestamp)

        self.assertIsInstance(actual, NistBeaconValue)
        self.assertTrue(actual.valid_signature)
        self.assertEqual(expected, actual)
        self.assertIsNot(expected, actual)
