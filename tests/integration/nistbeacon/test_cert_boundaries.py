"""
Copyright 2017 Peter Urda

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
from unittest.mock import patch

from nistbeacon import (
    NistBeacon,
    NistBeaconValue,
)
from nistbeacon.nistbeaconcrypto import NistBeaconCrypto
from tests.test_data.nist_records import local_record_json_db


class TestCertBoundaries(TestCase):
    @classmethod
    def setUpClass(cls):
        # Known verifiers
        cls.verifier2013 = "_VERIFIER_20130905"
        cls.verifier2017 = "_VERIFIER_20170808"

    def test_cert_20130905_start(self):
        timestamp = 1378395540
        expected_record = NistBeaconValue.from_json(
            local_record_json_db[timestamp]
        )

        with patch.object(NistBeaconCrypto, self.verifier2013) as mock:
            actual_record = NistBeacon.get_record(timestamp)
            self.assertEqual(mock.verify.call_count, 1)

        self.assertTrue(actual_record.valid_signature)
        self.assertEqual(expected_record, actual_record)

    def test_cert_20130905_end(self):
        timestamp = 1495837080
        expected_record = NistBeaconValue.from_json(
            local_record_json_db[timestamp]
        )

        with patch.object(NistBeaconCrypto, self.verifier2013) as mock:
            actual_record = NistBeacon.get_record(timestamp)
            self.assertEqual(mock.verify.call_count, 1)

        self.assertTrue(actual_record.valid_signature)
        self.assertEqual(expected_record, actual_record)

    def test_invalid_20170530_start(self):
        timestamp = 1496176860
        expected_record = NistBeaconValue.from_json(
            local_record_json_db[timestamp]
        )

        # Yeah this is gross, but these lines are so long with patch.object
        # All to verify that, well no verifiers are used during invalid
        # record lookups.
        #
        # So ugly :(
        #
        with \
                patch.object(NistBeaconCrypto, self.verifier2013) \
                as verifier2013, \
                patch.object(NistBeaconCrypto, self.verifier2017) \
                as verifier2017:
            actual_record = NistBeacon.get_record(timestamp)
            self.assertEqual(verifier2013.verify.call_count, 0)
            self.assertEqual(verifier2017.verify.call_count, 0)

        self.assertFalse(actual_record.valid_signature)
        self.assertEqual(expected_record, actual_record)

    def test_invalid_20170530_end(self):
        timestamp = 1502201640
        expected_record = NistBeaconValue.from_json(
            local_record_json_db[timestamp]
        )

        # Yeah this is gross, but these lines are so long with patch.object
        # All to verify that, well no verifiers are used during invalid
        # record lookups.
        #
        # So ugly :(
        #
        with \
                patch.object(NistBeaconCrypto, self.verifier2013) \
                as verifier2013, \
                patch.object(NistBeaconCrypto, self.verifier2017) \
                as verifier2017:
            actual_record = NistBeacon.get_record(timestamp)
            self.assertEqual(verifier2013.verify.call_count, 0)
            self.assertEqual(verifier2017.verify.call_count, 0)

        self.assertFalse(actual_record.valid_signature)
        self.assertEqual(expected_record, actual_record)

    def test_cert_20170808_start(self):
        timestamp = 1502202360
        expected_record = NistBeaconValue.from_json(
            local_record_json_db[timestamp]
        )

        with patch.object(NistBeaconCrypto, self.verifier2017) as mock:
            actual_record = NistBeacon.get_record(timestamp)
            self.assertEqual(mock.verify.call_count, 1)

        self.assertTrue(actual_record.valid_signature)
        self.assertEqual(expected_record, actual_record)

    def test_cert_20170808_end(self):
        with patch.object(NistBeaconCrypto, self.verifier2017) as mock:
            # Get last record, since this verifier is currently the
            # last known verifier.
            actual_record = NistBeacon.get_last_record()
            self.assertEqual(mock.verify.call_count, 1)

        self.assertTrue(actual_record.valid_signature)
