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
from tests.test_data.nist_records import local_record_db


# noinspection SpellCheckingInspection
class TestJson(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reference_record = local_record_db[1447873020]

    def test_frequency(self):
        expected = 60

        self.assertEqual(
            expected,
            self.reference_record.frequency,
        )

    def test_output_value(self):
        expected = (
            '2BE1468DF2E4081306002B9F9E344C7826DDC225583ED7FACC8804086867457DD'
            '4F4BD2DF9F5CE4B88DF6E30E4838F15168946BE18DFF596E667EC543AC08F54'
        )

        self.assertEqual(
            expected,
            self.reference_record.output_value,
        )

    def test_previous_output_value(self):
        expected = (
            'F4F571DFBA7DA2D3872AF1696B6A32B5039EB9CABF03CBB17EAB095D83B1483A1'
            '2CE2D0347BEAF2709CA0BAC0EB78C330D20CD3BE2FBEC2F7816AB2BB953AA3D'
        )

        self.assertEqual(
            expected,
            self.reference_record.previous_output_value,
        )

    def test_seed_value(self):
        expected = (
            '6189C4FF1F17ED41F9FF017CEB82DB2579193FBBB867B95E7FEBA52E74C937377'
            '626C522454C6223B25C007BF09C4B3AB55D24CFE1EB8F67C306FA75147E1CD2'
        )

        self.assertEqual(
            expected,
            self.reference_record.seed_value,
        )

    def test_signature_value(self):
        expected = (
            'F029F1A167DDBC17C041B9EB0A6AF2BC417D42C75001E39C2F9E2281AB9533B34'
            'ACBB584414AC10C20322F72C53D6425F3C595ECA31A0B26A23D0573DCA6DEADE0'
            '9D02214A7F9AF7EC0424D69B26EAF7269C648349AD189D90A43D67576BF4B0003'
            '5118F1AD939D228489A37EF822FEB04C2B4D1676B1041EC92883101150AAF7747'
            'EC88FE176BCA1B289E608E04CAF4CF47BE16A1B6243F8330E539740B9F6EB70A7'
            'A8E06777932B98617745AA2B545EFFA0DAA8DE016D00B55B01AEC91000508ACC4'
            '908D17A17311C68D156D63A03110250CB959A023BA75C700FE4EB43543DC1AC35'
            '781FF91D72AA7FE467F83569318C83D316801CC7159E83E2C306ADC2D'
        )

        self.assertEqual(
            expected,
            self.reference_record.signature_value,
        )

    def test_status_code(self):
        expected = '0'

        self.assertEqual(
            expected,
            self.reference_record.status_code,
        )

    def test_timestamp(self):
        expected = 1447873020

        self.assertEqual(
            expected,
            self.reference_record.timestamp,
        )

    def test_valid_signature(self):
        self.assertTrue(
            self.reference_record.valid_signature
        )

    def test_valid_signature_invalid(self):
        invalid_sig = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<record xmlns="http://beacon.nist.gov/record/0.1/">'
            '<version>Version 1.0</version>'
            '<frequency>60</frequency>'
            '<timeStamp>1447873020</timeStamp>'
            '<seedValue>'
            '00000000000000000000000000000000000000000000000000000000000000000'
            '00000000000000000000000000000000000000000000000000000000000000000'
            '</seedValue>'
            '<previousOutputValue>'
            'F4F571DFBA7DA2D3872AF1696B6A32B5039EB9CABF03CBB17EAB095D83B1483A1'
            '2CE2D0347BEAF2709CA0BAC0EB78C330D20CD3BE2FBEC2F7816AB2BB953AA3D'
            '</previousOutputValue>'
            '<signatureValue>'
            'F029F1A167DDBC17C041B9EB0A6AF2BC417D42C75001E39C2F9E2281AB9533B34'
            'ACBB584414AC10C20322F72C53D6425F3C595ECA31A0B26A23D0573DCA6DEADE0'
            '9D02214A7F9AF7EC0424D69B26EAF7269C648349AD189D90A43D67576BF4B0003'
            '5118F1AD939D228489A37EF822FEB04C2B4D1676B1041EC92883101150AAF7747'
            'EC88FE176BCA1B289E608E04CAF4CF47BE16A1B6243F8330E539740B9F6EB70A7'
            'A8E06777932B98617745AA2B545EFFA0DAA8DE016D00B55B01AEC91000508ACC4'
            '908D17A17311C68D156D63A03110250CB959A023BA75C700FE4EB43543DC1AC35'
            '781FF91D72AA7FE467F83569318C83D316801CC7159E83E2C306ADC2D'
            '</signatureValue>'
            '<outputValue>'
            '2BE1468DF2E4081306002B9F9E344C7826DDC225583ED7FACC8804086867457DD'
            '4F4BD2DF9F5CE4B88DF6E30E4838F15168946BE18DFF596E667E'
            'C543AC08F54'
            '</outputValue>'
            '<statusCode>0</statusCode>'
            '</record>'
        )

        invalid_sig_out = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<record xmlns="http://beacon.nist.gov/record/0.1/">'
            '<version>Version 1.0</version>'
            '<frequency>60</frequency>'
            '<timeStamp>1447873020</timeStamp>'
            '<seedValue>'
            '6189C4FF1F17ED41F9FF017CEB82DB2579193FBBB867B95E7FEBA52E74C937377'
            '626C522454C6223B25C007BF09C4B3AB55D24CFE1EB8F67C306FA75147E1CD2'
            '</seedValue>'
            '<previousOutputValue>'
            'F4F571DFBA7DA2D3872AF1696B6A32B5039EB9CABF03CBB17EAB095D83B1483A1'
            '2CE2D0347BEAF2709CA0BAC0EB78C330D20CD3BE2FBEC2F7816AB2BB953AA3D'
            '</previousOutputValue>'
            '<signatureValue>'
            'F029F1A167DDBC17C041B9EB0A6AF2BC417D42C75001E39C2F9E2281AB9533B34'
            'ACBB584414AC10C20322F72C53D6425F3C595ECA31A0B26A23D0573DCA6DEADE0'
            '9D02214A7F9AF7EC0424D69B26EAF7269C648349AD189D90A43D67576BF4B0003'
            '5118F1AD939D228489A37EF822FEB04C2B4D1676B1041EC92883101150AAF7747'
            'EC88FE176BCA1B289E608E04CAF4CF47BE16A1B6243F8330E539740B9F6EB70A7'
            'A8E06777932B98617745AA2B545EFFA0DAA8DE016D00B55B01AEC91000508ACC4'
            '908D17A17311C68D156D63A03110250CB959A023BA75C700FE4EB43543DC1AC35'
            '781FF91D72AA7FE467F83569318C83D316801CC7159E83E2C306ADC2D'
            '</signatureValue>'
            '<outputValue>'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
            '4F4BD2DF9F5CE4B88DF6E30E4838F15168946BE18DFF596E667E'
            'C543AC08F54'
            '</outputValue>'
            '<statusCode>0</statusCode>'
            '</record>'
        )

        # This should check when the data does not equal the signature
        self.assertFalse(
            NistBeaconValue.from_xml(
                invalid_sig,
            ).valid_signature
        )

        # This should check when the output doesn't match the hashed signature
        self.assertFalse(
            NistBeaconValue.from_xml(
                invalid_sig_out,
            ).valid_signature
        )

    def test_version(self):
        expected = "Version 1.0"

        self.assertEqual(
            expected,
            self.reference_record.version,
        )
