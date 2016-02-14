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

    def test_pseudo_random(self):
        """
        Check the seeding of NistBeaconValue's pseudo random property
        """

        init = NistBeaconValue.from_json(self.init_record.json)
        sample = NistBeaconValue.from_xml(self.sample_record.xml)

        # Basic object checking
        self.assertIsInstance(init, NistBeaconValue)
        self.assertIsInstance(sample, NistBeaconValue)

        self.assertIsInstance(init.pseudo_random, Random)
        self.assertIsInstance(sample.pseudo_random, Random)
        self.assertIsNot(
            init.pseudo_random,
            sample.pseudo_random,
        )

        # Verify that the pseudo random was seeded correctly
        # Init record check
        self.assertEqual(
            init.pseudo_random.random(),
            0.6461135178195806,
        )

        self.assertEqual(
            init.pseudo_random.uniform(100, 1000),
            973.057931801389,
        )

        self.assertEqual(
            init.pseudo_random.randrange(53, 350),
            230,
        )

        self.assertEqual(
            init.pseudo_random.randint(1000, 9999),
            4596,
        )

        # Sample value check
        self.assertEqual(
            sample.pseudo_random.random(),
            0.9150597089635818,
        )

        self.assertEqual(
            sample.pseudo_random.uniform(100, 1000),
            416.46104853317524,
        )

        self.assertEqual(
            sample.pseudo_random.randrange(53, 350),
            118,
        )

        self.assertEqual(
            sample.pseudo_random.randint(1000, 9999),
            7526,
        )
