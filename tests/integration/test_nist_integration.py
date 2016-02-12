from unittest import TestCase

from nistbeacon import (
    NistBeacon,
    NistBeaconValue,
)


class TestNistIntegration(TestCase):
    def setUp(self):
        self.target_timestamp = 1447873020

    # def test_get_last_record(self):
    #     pass
    #
    # def test_get_next(self):
    #     pass
    #
    # def test_get_previous(self):
    #     pass

    def test_get_record(self):
        downloaded = NistBeacon.get_last_record()

        self.assertIsInstance(
            obj=downloaded,
            cls=NistBeaconValue,
            msg="Did not download a NistBeaconValue"
        )

        self.assertTrue(
            expr=downloaded.valid_signature,
            msg="NistBeaconValue signature was invalid",
        )
