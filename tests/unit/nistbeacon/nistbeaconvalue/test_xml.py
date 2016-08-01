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
from tests.test_data.nist_records import (
    local_record_db,
    local_record_xml_db,
)


class TestXml(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.target_timestamp = 1447873020
        cls.target_record = local_record_db[cls.target_timestamp]
        cls.target_xml = local_record_xml_db[cls.target_timestamp]

    def test_from_xml(self):
        """
        Test building a beacon from XML
        """

        expected = self.target_record
        actual = NistBeaconValue.from_xml(self.target_xml)

        self.assertIsInstance(actual, NistBeaconValue)
        self.assertIsNot(expected, actual)
        self.assertEqual(expected, actual)

    def test_to_xml(self):
        """
        Test converting a beacon to XML
        """

        expected = self.target_xml
        actual = self.target_record.xml

        self.assertEqual(expected, actual)

    def test_from_xml_errors(self):
        """
        Verify that 'None' is generated correctly with invalid XML data
        """

        self.assertIsNone(
            NistBeaconValue.from_xml(
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<record>'
                'bad stuff ok'
            )
        )

        self.assertIsNone(
            NistBeaconValue.from_xml(
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<record>'
                '</record>'
            )
        )
