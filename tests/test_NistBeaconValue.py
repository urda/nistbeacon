from unittest import TestCase

from py_nist_beacon.nist_randomness_beacon_value import NistRandomnessBeaconValue


class TestNistBeaconValue(TestCase):
    # noinspection SpellCheckingInspection
    def setUp(self):
        # Configure the expected properties
        self.expected_frequency = int(60)
        self.expected_output_value = '2BE1468DF2E4081306002B9F9E344C7826DDC2' \
                                     '25583ED7FACC8804086867457DD4F4BD2DF9F5' \
                                     'CE4B88DF6E30E4838F15168946BE18DFF596E6' \
                                     '67EC543AC08F54'
        self.expected_previous_output_value = 'F4F571DFBA7DA2D3872AF1696B6A3' \
                                              '2B5039EB9CABF03CBB17EAB095D83' \
                                              'B1483A12CE2D0347BEAF2709CA0BA' \
                                              'C0EB78C330D20CD3BE2FBEC2F7816' \
                                              'AB2BB953AA3D'
        self.expected_seed_value = '6189C4FF1F17ED41F9FF017CEB82DB2579193FBB' \
                                   'B867B95E7FEBA52E74C937377626C522454C6223' \
                                   'B25C007BF09C4B3AB55D24CFE1EB8F67C306FA75' \
                                   '147E1CD2'
        self.expected_signature_value = 'F029F1A167DDBC17C041B9EB0A6AF2BC417' \
                                        'D42C75001E39C2F9E2281AB9533B34ACBB5' \
                                        '84414AC10C20322F72C53D6425F3C595ECA' \
                                        '31A0B26A23D0573DCA6DEADE09D02214A7F' \
                                        '9AF7EC0424D69B26EAF7269C648349AD189' \
                                        'D90A43D67576BF4B00035118F1AD939D228' \
                                        '489A37EF822FEB04C2B4D1676B1041EC928' \
                                        '83101150AAF7747EC88FE176BCA1B289E60' \
                                        '8E04CAF4CF47BE16A1B6243F8330E539740' \
                                        'B9F6EB70A7A8E06777932B98617745AA2B5' \
                                        '45EFFA0DAA8DE016D00B55B01AEC9100050' \
                                        '8ACC4908D17A17311C68D156D63A0311025' \
                                        '0CB959A023BA75C700FE4EB43543DC1AC35' \
                                        '781FF91D72AA7FE467F83569318C83D3168' \
                                        '01CC7159E83E2C306ADC2D'
        self.expected_status_code = '0'
        self.expected_timestamp = int(1447873020)
        self.expected_version = 'Version 1.0'

        # Invalid XML snippets for error testing
        self.sample_nist_parse_error = ('<?xml version="1.0" '
                                        'encoding="UTF-8" standalone="yes"?>'
                                        '<record>'
                                        'bad stuff ok'
                                        )

        self.sample_nist_missing_content = ('<?xml version="1.0" '
                                            'encoding="UTF-8" '
                                            'standalone="yes"?>'
                                            '<record>'
                                            '</record>'
                                            )

        # A full XML sample from the service
        self.sample_nist_xml = ('<?xml version="1.0" '
                                'encoding="UTF-8" standalone="yes"?>'
                                '<record>'
                                '<version>Version 1.0</version>'
                                '<frequency>60</frequency>'
                                '<timeStamp>1447873020</timeStamp>'
                                '<seedValue>'
                                '6189C4FF1F17ED41F9FF017CEB82DB2579193FBBB'
                                '867B95E7FEBA52E74C937377626C522454C6223B2'
                                '5C007BF09C4B3AB55D24CFE1EB8F67C306FA75147'
                                'E1CD2'
                                '</seedValue>'
                                '<previousOutputValue>'
                                'F4F571DFBA7DA2D3872AF1696B6A32B5039EB9CAB'
                                'F03CBB17EAB095D83B1483A12CE2D0347BEAF2709'
                                'CA0BAC0EB78C330D20CD3BE2FBEC2F7816AB2BB95'
                                '3AA3D'
                                '</previousOutputValue>'
                                '<signatureValue>'
                                'F029F1A167DDBC17C041B9EB0A6AF2BC417D42C75'
                                '001E39C2F9E2281AB9533B34ACBB584414AC10C20'
                                '322F72C53D6425F3C595ECA31A0B26A23D0573DCA'
                                '6DEADE09D02214A7F9AF7EC0424D69B26EAF7269C'
                                '648349AD189D90A43D67576BF4B00035118F1AD93'
                                '9D228489A37EF822FEB04C2B4D1676B1041EC9288'
                                '3101150AAF7747EC88FE176BCA1B289E608E04CAF'
                                '4CF47BE16A1B6243F8330E539740B9F6EB70A7A8E'
                                '06777932B98617745AA2B545EFFA0DAA8DE016D00'
                                'B55B01AEC91000508ACC4908D17A17311C68D156D'
                                '63A03110250CB959A023BA75C700FE4EB43543DC1'
                                'AC35781FF91D72AA7FE467F83569318C83D316801'
                                'CC7159E83E2C306ADC2D'
                                '</signatureValue>'
                                '<outputValue>'
                                '2BE1468DF2E4081306002B9F9E344C7826DDC2255'
                                '83ED7FACC8804086867457DD4F4BD2DF9F5CE4B88'
                                'DF6E30E4838F15168946BE18DFF596E667EC543AC'
                                '08F54'
                                '</outputValue>'
                                '<statusCode>0</statusCode>'
                                '</record>'
                                )

    def object_value_test(self, nist_beacon: NistRandomnessBeaconValue):
        """
        Given a NIST Random Value Beacon,
        verify the object properties are correct

        :param nist_beacon: The NIST beacon to check
        """

        # Verify a value was actually created
        self.assertIsInstance(nist_beacon, NistRandomnessBeaconValue)

        # Verify values
        self.assertEqual(nist_beacon.frequency, self.expected_frequency)
        self.assertEqual(nist_beacon.output_value, self.expected_output_value)
        self.assertEqual(
            nist_beacon.previous_output_value,
            self.expected_previous_output_value
        )
        self.assertEqual(nist_beacon.seed_value, self.expected_seed_value)
        self.assertEqual(
            nist_beacon.signature_value,
            self.expected_signature_value
        )
        self.assertEqual(nist_beacon.status_code, self.expected_status_code)
        self.assertEqual(nist_beacon.timestamp, self.expected_timestamp)
        self.assertEqual(nist_beacon.version, self.expected_version)

    def test_from_xml(self):
        """
        Test construction from XML
        """

        self.object_value_test(NistRandomnessBeaconValue.from_xml(self.sample_nist_xml))

    def test_init(self):
        """
        Test the object's init method
        """

        self.object_value_test(NistRandomnessBeaconValue(
            version=self.expected_version,
            frequency=self.expected_frequency,
            timestamp=self.expected_timestamp,
            seed_value=self.expected_seed_value,
            previous_output_value=self.expected_previous_output_value,
            signature_value=self.expected_signature_value,
            output_value=self.expected_output_value,
            status_code=self.expected_status_code,
        ))

    def test_xml_error_handling(self):
        """
        Verify that 'None' is generated correctly with invalid XML data
        """

        self.assertIsNone(
            NistRandomnessBeaconValue.from_xml(self.sample_nist_parse_error)
        )

        self.assertIsNone(
            NistRandomnessBeaconValue.from_xml(self.sample_nist_missing_content)
        )
