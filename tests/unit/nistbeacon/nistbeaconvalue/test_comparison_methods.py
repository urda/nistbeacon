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

from nistbeacon import NistBeaconValue
from tests.test_data.nist_records import local_record_json_db


class TestComparisonMethods(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record_a = local_record_json_db[1447872960]
        cls.record_b = local_record_json_db[1447873020]

        # Perform conversions from json data to record objects
        cls.record_a = NistBeaconValue.from_json(cls.record_a)
        cls.record_b = NistBeaconValue.from_json(cls.record_b)

    def test_eq(self):
        """
        Verify "equals" operation
        """
        expected = self.record_a
        new_record_obj = NistBeaconValue.from_xml(expected.xml)

        self.assertFalse(expected is new_record_obj)
        self.assertEqual(expected, new_record_obj)

    def test_eq_exception(self):
        """
        Verify "equals" operation returns without AttributeError or TypeError
        """
        self.assertFalse(self.record_b == 0)
        self.assertFalse(self.record_b == '')
        self.assertTrue(self.record_b != '')

    def test_neq(self):
        """
        Verify "not equal" operation
        """
        self.assertNotEqual(self.record_a, self.record_b)
