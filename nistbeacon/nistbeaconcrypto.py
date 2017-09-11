"""
Copyright 2015-2017 Peter Urda

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

import binascii
import struct

from Crypto.Hash import SHA512
from Crypto.Hash.SHA512 import SHA512Hash
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class NistBeaconCrypto(object):
    """
    Helper class to handle beacon value signature and crypto checks.
    """

    # https://beacon.nist.gov/certificate/beacon.cer
    # noinspection SpellCheckingInspection
    _NIST_CER_FILE_20130905 = (
        '-----BEGIN CERTIFICATE-----\n'
        'MIIHZTCCBk2gAwIBAgIESTWNPjANBgkqhkiG9w0BAQsFADBtMQswCQYDVQQGEwJV\n'
        'UzEQMA4GA1UEChMHRW50cnVzdDEiMCAGA1UECxMZQ2VydGlmaWNhdGlvbiBBdXRo\n'
        'b3JpdGllczEoMCYGA1UECxMfRW50cnVzdCBNYW5hZ2VkIFNlcnZpY2VzIFNTUCBD\n'
        'QTAeFw0xNDA1MDcxMzQ4MzZaFw0xNzA1MDcxNDE4MzZaMIGtMQswCQYDVQQGEwJV\n'
        'UzEYMBYGA1UEChMPVS5TLiBHb3Zlcm5tZW50MR8wHQYDVQQLExZEZXBhcnRtZW50\n'
        'IG9mIENvbW1lcmNlMTcwNQYDVQQLEy5OYXRpb25hbCBJbnN0aXR1dGUgb2YgU3Rh\n'
        'bmRhcmRzIGFuZCBUZWNobm9sb2d5MRAwDgYDVQQLEwdEZXZpY2VzMRgwFgYDVQQD\n'
        'Ew9iZWFjb24ubmlzdC5nb3YwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB\n'
        'AQC/m2xcckaSYztt6/6YezaUmqIqY5CLvrfO2esEIJyFg+cv7S7exL3hGYeDCnQL\n'
        'VtUIGViAnO9yCXDC2Kymen+CekU7WEtSB96xz/xGrY3mbwjS46QSOND9xSRMroF9\n'
        'xbgqXxzJ7rL/0RMUkku3uurGb/cxUpzKt6ra7iUnzkk3BBk73kr2OXFyYYbtrN71\n'
        's0B9qKKJZuPQqmA5n80Xc3E2YbaoAW4/gesncFNL7Sdxw9NIA1L4feu/o8xp3FNP\n'
        'pv2e25C0113x+yagvb1W0mw6ISwAKhJ+6G4t4hFejl7RujuiDfORgzIhHMR4CyWt\n'
        'PZFVn2qxZuVooj1+mduLIXhDAgMBAAGjggPKMIIDxjAOBgNVHQ8BAf8EBAMCBsAw\n'
        'FwYDVR0gBBAwDjAMBgpghkgBZQMCAQMHMIIBXgYIKwYBBQUHAQEEggFQMIIBTDCB\n'
        'uAYIKwYBBQUHMAKGgatsZGFwOi8vc3NwZGlyLm1hbmFnZWQuZW50cnVzdC5jb20v\n'
        'b3U9RW50cnVzdCUyME1hbmFnZWQlMjBTZXJ2aWNlcyUyMFNTUCUyMENBLG91PUNl\n'
        'cnRpZmljYXRpb24lMjBBdXRob3JpdGllcyxvPUVudHJ1c3QsYz1VUz9jQUNlcnRp\n'
        'ZmljYXRlO2JpbmFyeSxjcm9zc0NlcnRpZmljYXRlUGFpcjtiaW5hcnkwSwYIKwYB\n'
        'BQUHMAKGP2h0dHA6Ly9zc3B3ZWIubWFuYWdlZC5lbnRydXN0LmNvbS9BSUEvQ2Vy\n'
        'dHNJc3N1ZWRUb0VNU1NTUENBLnA3YzBCBggrBgEFBQcwAYY2aHR0cDovL29jc3Au\n'
        'bWFuYWdlZC5lbnRydXN0LmNvbS9PQ1NQL0VNU1NTUENBUmVzcG9uZGVyMBsGA1Ud\n'
        'CQQUMBIwEAYJKoZIhvZ9B0QdMQMCASIwggGHBgNVHR8EggF+MIIBejCB6qCB56CB\n'
        '5IaBq2xkYXA6Ly9zc3BkaXIubWFuYWdlZC5lbnRydXN0LmNvbS9jbj1XaW5Db21i\n'
        'aW5lZDEsb3U9RW50cnVzdCUyME1hbmFnZWQlMjBTZXJ2aWNlcyUyMFNTUCUyMENB\n'
        'LG91PUNlcnRpZmljYXRpb24lMjBBdXRob3JpdGllcyxvPUVudHJ1c3QsYz1VUz9j\n'
        'ZXJ0aWZpY2F0ZVJldm9jYXRpb25MaXN0O2JpbmFyeYY0aHR0cDovL3NzcHdlYi5t\n'
        'YW5hZ2VkLmVudHJ1c3QuY29tL0NSTHMvRU1TU1NQQ0ExLmNybDCBiqCBh6CBhKSB\n'
        'gTB/MQswCQYDVQQGEwJVUzEQMA4GA1UEChMHRW50cnVzdDEiMCAGA1UECxMZQ2Vy\n'
        'dGlmaWNhdGlvbiBBdXRob3JpdGllczEoMCYGA1UECxMfRW50cnVzdCBNYW5hZ2Vk\n'
        'IFNlcnZpY2VzIFNTUCBDQTEQMA4GA1UEAxMHQ1JMNjY3MzArBgNVHRAEJDAigA8y\n'
        'MDE0MDUwNzEzNDgzNlqBDzIwMTYwNjEyMTgxODM2WjAfBgNVHSMEGDAWgBTTzudb\n'
        'iafNbJHGZzapWHIJ7OI58zAdBgNVHQ4EFgQUGIOcf6r7Z9wk+2/YuG5oTs7Qwk8w\n'
        'CQYDVR0TBAIwADAZBgkqhkiG9n0HQQAEDDAKGwRWOC4xAwIEsDANBgkqhkiG9w0B\n'
        'AQsFAAOCAQEASc+lZBbJWsHB2WnaBr8ZfBqpgS51Eh+wLchgIq7JHhVn+LagkR8C\n'
        'XmvP57a0L/E+MRBqvH2RMqwthEcjXio2WIu/lyKZmg2go9driU6H3s89X8snblDF\n'
        '1B+iL73vhkLVdHXgStMS8AHbm+3BW6yjHens1tVmKSowg1P/bGT3Z4nmamdY9oLm\n'
        '9sCgFccthC1BQqtPv1XsmLshJ9vmBbYMsjKq4PmS0aLA59J01YMSq4U1kzcNS7wI\n'
        '1/YfUrfeV+r+j7LKBgNQTZ80By2cfSalEqCe8oxqViAz6DsfPCBeE57diZNLiJmj\n'
        'a2wWIBquIAXxvD8w2Bue7pZVeUHls5V5dA==\n'
        '-----END CERTIFICATE-----\n'
    )

    # https://beacon.nist.gov/certificate/beacon.cer
    # noinspection SpellCheckingInspection
    _NIST_RSA_KEY_20130905 = (
        '-----BEGIN PUBLIC KEY-----\n'
        'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv5tsXHJGkmM7bev+mHs2\n'
        'lJqiKmOQi763ztnrBCCchYPnL+0u3sS94RmHgwp0C1bVCBlYgJzvcglwwtispnp/\n'
        'gnpFO1hLUgfesc/8Rq2N5m8I0uOkEjjQ/cUkTK6BfcW4Kl8cye6y/9ETFJJLt7rq\n'
        'xm/3MVKcyreq2u4lJ85JNwQZO95K9jlxcmGG7aze9bNAfaiiiWbj0KpgOZ/NF3Nx\n'
        'NmG2qAFuP4HrJ3BTS+0nccPTSANS+H3rv6PMadxTT6b9ntuQtNdd8fsmoL29VtJs\n'
        'OiEsACoSfuhuLeIRXo5e0bo7og3zkYMyIRzEeAslrT2RVZ9qsWblaKI9fpnbiyF4\n'
        'QwIDAQAB\n'
        '-----END PUBLIC KEY-----\n'
    )

    _RSA_KEY_20130905 = RSA.importKey(_NIST_RSA_KEY_20130905)
    _VERIFIER_20130905 = PKCS1_v1_5.new(_RSA_KEY_20130905)

    @classmethod
    def get_hash(
            cls,
            version: str,
            frequency: int,
            timestamp: int,
            seed_value: str,
            prev_output: str,
            status_code: str,
    ) -> SHA512Hash:
        """
        Given required properties from a NistBeaconValue,
        compute the SHA512Hash object.

        :param version: NistBeaconValue.version
        :param frequency: NistBeaconValue.frequency
        :param timestamp: NistBeaconValue.timestamp
        :param seed_value: NistBeaconValue.seed_value
        :param prev_output: NistBeaconValue.previous_output_value
        :param status_code: NistBeaconValue.status_code

        :return: SHA512 Hash for NistBeaconValue signature verification
        """
        return SHA512.new(
            version.encode() +
            struct.pack(
                '>1I1Q64s64s1I',
                frequency,
                timestamp,
                binascii.a2b_hex(seed_value),
                binascii.a2b_hex(prev_output),
                int(status_code),
            )
        )

    @classmethod
    def verify(
            cls,
            timestamp: int,
            message_hash: SHA512Hash,
            signature: bytes,
    ) -> bool:
        """
        Verify a given NIST message hash and signature for a beacon value.

        :param timestamp: The timestamp of the record being verified.
        :param message_hash:
            The hash that was carried out over the message.
            This is an object belonging to the `Crypto.Hash` module.
        :param signature: The signature that needs to be validated.
        :return: True if verification is correct. False otherwise.
        """

        result = cls._VERIFIER_20130905.verify(
            message_hash,
            signature,
        )

        # Convert 1 to 'True', 'False' otherwise
        if isinstance(result, int):
            result = True if result == 1 else False

        return result
