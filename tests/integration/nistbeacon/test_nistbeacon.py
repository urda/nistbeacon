"""
Copyright 2015-2016 Peter Urda

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

from nistbeacon import NistBeacon
from tests.test_data.nist_records import local_record_db


class TestNistIntegration(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.future_timestamp = 32503680000
        cls.future_record = local_record_db[cls.future_timestamp]

        cls.target_timestamp = 1447873020

        cls.focus_record = local_record_db[cls.target_timestamp]
        cls.next_record = local_record_db[cls.target_timestamp + 60]
        cls.previous_record = local_record_db[cls.target_timestamp - 60]

    def test_get_last_record(self):
        actual = NistBeacon.get_last_record()

        self.assertTrue(actual.valid_signature)

    def test_get_next(self):
        expected = self.next_record
        actual = NistBeacon.get_next(self.target_timestamp)

        self.assertTrue(actual.valid_signature)
        self.assertEqual(expected, actual)
        self.assertIsNot(expected, actual)

    def test_get_previous(self):
        expected = self.previous_record
        actual = NistBeacon.get_previous(self.target_timestamp)

        self.assertTrue(actual.valid_signature)
        self.assertEqual(expected, actual)
        self.assertIsNot(expected, actual)

    def test_get_record(self):
        expected = self.focus_record
        actual = NistBeacon.get_record(self.target_timestamp)

        self.assertTrue(actual.valid_signature)
        self.assertEqual(expected, actual)
        self.assertIsNot(expected, actual)

    def test_get_record_404(self):
        expected = self.future_record
        actual = NistBeacon.get_record(self.future_timestamp)

        self.assertIsNone(actual)
        self.assertEqual(expected, actual)
