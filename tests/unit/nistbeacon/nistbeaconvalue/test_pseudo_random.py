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

from random import Random
from unittest import TestCase

from nistbeacon import NistBeaconValue
from tests.test_data.nist_records import local_record_db


class TestPseudoRandom(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.init_record = local_record_db[1378395540]
        cls.sample_record = local_record_db[1447873020]

    def test_init_record_random_values(self):
        """
        Check the seeding of NistBeaconValue's pseudo random property.

        This is for the known initial record.
        """

        record = self.init_record

        self.assertIsInstance(record, NistBeaconValue)
        self.assertIsInstance(record.pseudo_random, Random)

        # Verify that the pseudo random was seeded correctly
        self.assertEqual(
            record.pseudo_random.random(),
            0.6461135178195806,
        )

        self.assertEqual(
            record.pseudo_random.uniform(100, 1000),
            973.057931801389,
        )

        self.assertEqual(
            record.pseudo_random.randrange(53, 350),
            230,
        )

        self.assertEqual(
            record.pseudo_random.randint(1000, 9999),
            4596,
        )

    def test_sample_record_random_values(self):
        """
        Check the seeding of NistBeaconValue's pseudo random property

        This is for the reference testing record
        """

        record = self.sample_record

        self.assertIsInstance(record, NistBeaconValue)
        self.assertIsInstance(record.pseudo_random, Random)

        # Verify that the pseudo random was seeded correctly
        self.assertEqual(
            record.pseudo_random.random(),
            0.9150597089635818,
        )

        self.assertEqual(
            record.pseudo_random.uniform(100, 1000),
            416.46104853317524,
        )

        self.assertEqual(
            record.pseudo_random.randrange(53, 350),
            118,
        )

        self.assertEqual(
            record.pseudo_random.randint(1000, 9999),
            7526,
        )
