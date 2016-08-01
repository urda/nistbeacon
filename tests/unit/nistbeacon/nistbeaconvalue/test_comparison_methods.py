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

from nistbeacon import NistBeaconValue
from tests.test_data.nist_records import local_record_db


class TestComparisonMethods(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record_1447872960 = local_record_db[1447872960]
        cls.record_1447873020 = local_record_db[1447873020]

    def test_eq(self):
        """
        Verify "equals" operation
        """

        expected = self.record_1447872960
        new_record_obj = NistBeaconValue.from_xml(expected.xml)

        self.assertFalse(expected is new_record_obj)
        self.assertEqual(expected, new_record_obj)

    def test_eq_exception(self):
        """
        Verify "equals" operation returns without AttributeError or TypeError
        """

        self.assertFalse(self.record_1447873020 == 0)
        self.assertFalse(self.record_1447873020 == '')
        self.assertTrue(self.record_1447873020 != '')

    def test_neq(self):
        """
        Verify "not equal" operation
        """

        self.assertNotEqual(
            self.record_1447872960,
            self.record_1447873020,
        )
