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

from nistbeacon.nistbeaconcrypto import NistBeaconCrypto
from unittest.mock import (
    Mock,
    patch,
)


class TestNistBeaconCrypto(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.verifier2013 = "_VERIFIER_20130905"
        cls.verifier2013_timestamp = 1378395540

    def test_verify_converts_1_to_bool(self):
        """
        Verify that the verify method converts any positive (excluding 1)
        value to a 'False' bool.
        """
        # Create a mock'd verifier
        mock_verifier = Mock()
        mock_verifier.verify = Mock(return_value=1)

        with patch.object(NistBeaconCrypto, self.verifier2013, mock_verifier):
            # noinspection PyTypeChecker
            result = NistBeaconCrypto.verify(
                self.verifier2013_timestamp,
                "junk",
                "data",
            )

            self.assertIsInstance(result, bool)
            self.assertTrue(result)

    def test_verify_converts_false_int_to_bool(self):
        """
        Verify that the verify method converts any integer
        value EXCEPT FOR 1 to a 'False' bool.
        """
        test_data = [100, 10, 2, 0, -2, -10, -100]

        # Create a mock'd verifier
        mock_verifier = Mock()
        mock_verifier.verify = Mock(side_effect=test_data)

        with patch.object(NistBeaconCrypto, self.verifier2013, mock_verifier):
            for _ in test_data:
                # noinspection PyTypeChecker
                result = NistBeaconCrypto.verify(
                    self.verifier2013_timestamp,
                    "junk",
                    "data",
                )

                self.assertIsInstance(result, bool)
                self.assertFalse(result)

    def test_verify_does_not_convert_bool(self):
        """
        Verify that the verify method does not convert any bool value
        """
        test_data = [False, True]

        # Create a mock'd verifier
        mock_verifier = Mock()
        mock_verifier.verify = Mock(side_effect=test_data)

        with patch.object(NistBeaconCrypto, self.verifier2013, mock_verifier):
            for test_data_point in test_data:
                # noinspection PyTypeChecker
                result = NistBeaconCrypto.verify(
                    self.verifier2013_timestamp,
                    "junk",
                    "data",
                )

                self.assertIsInstance(result, bool)
                self.assertEqual(test_data_point, result)
