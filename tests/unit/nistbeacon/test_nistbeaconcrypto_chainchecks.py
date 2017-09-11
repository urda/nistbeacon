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

from nistbeacon import NistBeaconValue
from tests.test_data.nist_records import local_record_json_db


class TestNistBeaconCryptoChainChecks(TestCase):
    """
    See also: https://github.com/urda/nistbeacon/issues/26
    """

    def test_cert_20130905_start(self):
        """
        Test the start of records that are signed with the 2013-09-05 cert.
        """
        record = NistBeaconValue.from_json(local_record_json_db[1378395540])
        self.assertTrue(record.valid_signature)

    def test_cert_20130905_end(self):
        """
        Test the end of records that are signed with the 2013-09-05 cert.
        """
        record = NistBeaconValue.from_json(local_record_json_db[1495837080])
        self.assertTrue(record.valid_signature)

    def test_invalid_20170530_start(self):
        """
        Test the start of records that are considered bugged by NIST.
        """
        record = NistBeaconValue.from_json(local_record_json_db[1496176860])
        self.assertFalse(record.valid_signature)

    def test_invalid_20170530_end(self):
        """
        Test the end of records that are considered bugged by NIST.
        """
        record = NistBeaconValue.from_json(local_record_json_db[1502201640])
        self.assertFalse(record.valid_signature)

    def test_cert_20170808_start(self):
        """
        Test the start of records that are signed with the 2017-08-08 cert.
        """
        record = NistBeaconValue.from_json(local_record_json_db[1502202360])
        self.assertTrue(record.valid_signature)

    def test_cert_20170808_end(self):
        """
        Test the end (at time of test creation) records that are signed with
        the 2017-08-08 cert.
        """
        record = NistBeaconValue.from_json(local_record_json_db[1505097420])
        self.assertTrue(record.valid_signature)
