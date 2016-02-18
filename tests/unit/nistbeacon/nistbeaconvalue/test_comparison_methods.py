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
    local_record_xml_db,
)


class TestNistBeaconValue(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reference_record_xml = local_record_xml_db[1447873020]

    def test_equality_operators(self):
        """
        Verify the "equals" and "not equals" operators
        are working correctly
        """

        from_xml = NistBeaconValue.from_xml(self.reference_record_xml)

        from_props = NistBeaconValue(
            version=from_xml.version,
            frequency=from_xml.frequency,
            timestamp=from_xml.timestamp,
            seed_value=from_xml.seed_value,
            previous_output_value=from_xml.previous_output_value,
            signature_value=from_xml.signature_value,
            output_value=from_xml.output_value,
            status_code=from_xml.status_code,
        )

        # These should be two different objects
        self.assertFalse(from_props is from_xml)

        # But they should be consider "equal"
        self.assertTrue(from_props == from_xml)

        # Which should return "False" when asked if they are not equal
        self.assertFalse(from_props != from_xml)

        # As well as when compared to wrong things
        self.assertFalse(from_props == '')
        self.assertTrue(from_props != '')
