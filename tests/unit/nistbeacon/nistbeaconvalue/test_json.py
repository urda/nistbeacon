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

import json
from unittest import TestCase

from nistbeacon import NistBeaconValue
from tests.test_data.nist_records import (
    local_record_db,
    local_record_json_db,
)


class TestJson(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.target_timestamp = 1447873020
        cls.target_record = local_record_db[cls.target_timestamp]
        cls.target_json = local_record_json_db[cls.target_timestamp]

    def test_from_json(self):
        """
        Test building a beacon from JSON
        """

        expected = self.target_record
        actual = NistBeaconValue.from_json(self.target_json)

        self.assertIsInstance(actual, NistBeaconValue)
        self.assertIsNot(expected, actual)
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """
        Test converting a beacon to JSON
        """

        expected = json.loads(self.target_json)
        actual = json.loads(self.target_record.json)

        self.assertCountEqual(expected, actual)

        for actual_key, actual_value in actual.items():
            self.assertEqual(
                expected[actual_key],
                actual_value,
            )
