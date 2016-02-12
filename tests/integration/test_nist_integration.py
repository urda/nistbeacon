from unittest import TestCase

from nistbeacon import (
    NistBeacon,
    NistBeaconValue,
)


class TestNistIntegration(TestCase):
    def setUp(self):
        self.target_timestamp = 1447873020

        self.focus_record = NistBeaconValue(
            version='Version 1.0',
            frequency=int(60),
            timestamp=int(1447873020),
            seed_value='6189C4FF1F17ED41F9FF017CEB82DB2579193FBBB867B95E7FEBA5'
                       '2E74C937377626C522454C6223B25C007BF09C4B3AB55D24CFE1EB'
                       '8F67C306FA75147E1CD2',
            previous_output_value='F4F571DFBA7DA2D3872AF1696B6A32B5039EB9CABF0'
                                  '3CBB17EAB095D83B1483A12CE2D0347BEAF2709CA0B'
                                  'AC0EB78C330D20CD3BE2FBEC2F7816AB2BB953AA3D',
            signature_value='F029F1A167DDBC17C041B9EB0A6AF2BC417D42C75001E39C2'
                            'F9E2281AB9533B34ACBB584414AC10C20322F72C53D6425F3'
                            'C595ECA31A0B26A23D0573DCA6DEADE09D02214A7F9AF7EC0'
                            '424D69B26EAF7269C648349AD189D90A43D67576BF4B00035'
                            '118F1AD939D228489A37EF822FEB04C2B4D1676B1041EC928'
                            '83101150AAF7747EC88FE176BCA1B289E608E04CAF4CF47BE'
                            '16A1B6243F8330E539740B9F6EB70A7A8E06777932B986177'
                            '45AA2B545EFFA0DAA8DE016D00B55B01AEC91000508ACC490'
                            '8D17A17311C68D156D63A03110250CB959A023BA75C700FE4'
                            'EB43543DC1AC35781FF91D72AA7FE467F83569318C83D3168'
                            '01CC7159E83E2C306ADC2D',
            output_value='2BE1468DF2E4081306002B9F9E344C7826DDC225583ED7FACC88'
                         '04086867457DD4F4BD2DF9F5CE4B88DF6E30E4838F15168946BE'
                         '18DFF596E667EC543AC08F54',
            status_code='0',
        )

    def test_get_last_record(self):
        actual = NistBeacon.get_last_record()

        self.assertIsInstance(actual, NistBeaconValue)
        self.assertTrue(actual.valid_signature)

    # def test_get_next(self):
    #     pass
    #
    # def test_get_previous(self):
    #     pass

    def test_get_record(self):
        expected = self.focus_record
        actual = NistBeacon.get_record(self.target_timestamp)

        self.assertIsInstance(actual, NistBeaconValue)
        self.assertTrue(actual.valid_signature)
        self.assertEqual(expected, actual)
        self.assertIsNot(expected, actual)
