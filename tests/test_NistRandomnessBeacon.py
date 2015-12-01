from unittest import TestCase
from unittest.mock import (
    Mock,
    patch,
)

import requests.exceptions

import py_nist_beacon.nist_beacon_constants as cn
from py_nist_beacon import NistRandomnessBeacon
from py_nist_beacon.nist_randomness_beacon_value import (
    NistRandomnessBeaconValue
)


class TestNistRandomnessBeacon(TestCase):
    # noinspection SpellCheckingInspection
    def setUp(self):
        self.reference_timestamp = int(1447873020)

        self.expected_current = NistRandomnessBeaconValue(
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

        self.expected_next = NistRandomnessBeaconValue(
            version='Version 1.0',
            frequency=int(60),
            timestamp=int(1447873080),
            seed_value='7C82286A7198A052775066CA19AA08D13DF50E7B9B917C54C08AD5'
                       '8A888EFDDC74420794D5D6FACD9BCC23FF389B8C64F4B253F2029E'
                       '4B8B5DD40522C6A79C31',
            previous_output_value='2BE1468DF2E4081306002B9F9E344C7826DDC225583'
                                  'ED7FACC8804086867457DD4F4BD2DF9F5CE4B88DF6E'
                                  '30E4838F15168946BE18DFF596E667EC543AC08F54',
            signature_value='6866B8D248BE52FE8F07AEA0E6CFEA491C4161B798C72F3AF'
                            '029BAC311CEA393ECEC11709F45850BFB39DF272B8B14F6A3'
                            'A99493191FADF6F93BD50D3985049D0396A4603D45A332051'
                            '23E02FF4BC4ECEB4C253F08EEEE6C44F70BA64A7C4AC46DF0'
                            'C981A21827CF0A9FD3CFB1E9160C284FA73C71508603103EA'
                            '5A9806C8850C773CCEC60E19BC9B5D1E6BA4A628C5016FEC7'
                            '410FF2A47CB00B33AFFD6A40155282405735E3DE12D94B851'
                            'A7174A4058766EF696244CBBD237BB991F947E69ABED1FEB0'
                            '6BA061319D4D95C911F9EBFAC57012DA6145B2E4AE325B8B4'
                            '6653E85335F804770CFC2EC4A54DADF49E628C657122B24A0'
                            '1025349578BE8E1E5C3B6B',
            output_value='7C4C052130AF855FC7B05B03E7C06C6CF6613A60698931DD438A'
                         'CE70E3F65346DA089114DC8A334510FF86C7692B9F54F25653B6'
                         '30FB8E36209A45EF864C426F',
            status_code='0',
        )

        self.expected_previous = NistRandomnessBeaconValue(
            version='Version 1.0',
            frequency=int(60),
            timestamp=int(1447872960),
            seed_value='7DFDD1BD78543254B0DDA92893A83B190BB5FD8D56308F0F39256E'
                       '6796BE43A81C6A94FDA51DB66E23B31CB146BB3626CC5CE46AEDD3'
                       '16F723053542F28E1F26',
            previous_output_value='87F0184434F9670DEF77406A52300F76E363FC78598'
                                  '52EBD381736F04013BD1B37697F305AB540911006FF'
                                  '6B1B29598B5FE730AE57A65F00A0C94748FCB83138',
            signature_value='E8F6A08CA36B87D0B4667EEB592CA46F96F84CBD6F44BCAB6'
                            'AA29CAC09966804925B85FB6835FD35C5789A1544A7F9B836'
                            '5098CA439E7C461221D74362B5261B154FC4BAB56788A6F5C'
                            '3AE642EF750D6712DAC4E5742A7B598C80C160F73FBA88D9D'
                            '03B06D66C8AE90EF03E6717ECA4A535F1082417A73BAB7717'
                            '1EDD19A8E5272B181E87BCE9D9DBABD3CB05EB778162CD4B9'
                            'C637A237C1ED54B80AB28AF2846AB6B70A1935BC41EDB4DA2'
                            'A5EE0AB511504C8299692CDB9316220CE7D71AB3F479F251E'
                            'F65ED100A59937F4509D71464593C513799927EF7AC734CB2'
                            '7ECB1D008E2F5DC481A19D9AF4EC97E014356A9B76F190456'
                            '33742E2C2D3426B6CB5C74',
            output_value='F4F571DFBA7DA2D3872AF1696B6A32B5039EB9CABF03CBB17EAB'
                         '095D83B1483A12CE2D0347BEAF2709CA0BAC0EB78C330D20CD3B'
                         'E2FBEC2F7816AB2BB953AA3D',
            status_code='0',
        )

    def test_get_next(self):
        next_record = NistRandomnessBeacon.get_next(self.reference_timestamp)
        self.assertEqual(self.expected_next, next_record)

    def test_get_previous(self):
        previous_record = NistRandomnessBeacon.get_previous(
            self.reference_timestamp
        )
        self.assertEqual(self.expected_previous, previous_record)

    def test_get_record(self):
        record = NistRandomnessBeacon.get_record(self.reference_timestamp)
        self.assertEqual(self.expected_current, record)

    def test_get_last_record(self):
        last_record = NistRandomnessBeacon.get_last_record()

        self.assertIsInstance(last_record, NistRandomnessBeaconValue)

    def test_get_last_record_404(self):
        with patch('requests.get') as patched_requests:
            mock_response = Mock()
            mock_response.status_code = 404
            patched_requests.return_value = mock_response

            self.assertIsNone(NistRandomnessBeacon.get_last_record())

    def test_get_last_record_exceptions(self):
        exceptions_to_test = [
            requests.exceptions.RequestException(),
            requests.exceptions.ConnectionError(),
            requests.exceptions.HTTPError(),
            requests.exceptions.URLRequired(),
            requests.exceptions.TooManyRedirects(),
            requests.exceptions.Timeout(),
        ]

        for exception_to_test in exceptions_to_test:
            with patch('requests.get') as patched_requests:
                patched_requests.side_effect = exception_to_test
                self.assertIsNone(NistRandomnessBeacon.get_last_record())

    def test_chain_check_none(self):
        # noinspection PyTypeChecker
        self.assertFalse(NistRandomnessBeacon.chain_check(None))

    def test_chain_check_majority(self):
        self.assertTrue(
            NistRandomnessBeacon.chain_check(
                self.expected_current
            )
        )

    def test_chain_check_init(self):
        test_init = NistRandomnessBeaconValue.from_json(
            cn.NIST_INIT_RECORD,
        )

        self.assertTrue(
            NistRandomnessBeacon.chain_check(
                test_init
            )
        )

    def test_chain_check_last(self):
        # POTENTIAL RACE CONDITION!
        # Get last record -> pass to method ->
        # no longer last before chain check complete
        # Should this be patched?

        self.assertTrue(
            NistRandomnessBeacon.chain_check(
                NistRandomnessBeacon.get_last_record(),
            )
        )
