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

from Crypto.Hash import SHA512
from Crypto.Hash.SHA512 import SHA512Hash
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import nistbeacon.constants as cn


class NistBeaconCrypto(object):
    """
    Helper class to handle beacon value signature and crypto checks.
    """

    _rsa_key = RSA.importKey(cn.NIST_RSA_KEY)
    _verifier = PKCS1_v1_5.new(_rsa_key)

    @classmethod
    def get_hash(cls, byte_string: bytes) -> SHA512Hash:
        """
        Given the byte string from a NistBeaconValue,
        compute the SHA512Hash object.

        The bytes should look like:

        version.encode() +
        struct.pack(
            '>1I1Q64s64s1I',
            frequency,
            timestamp,
            binascii.a2b_hex(seed_value),
            binascii.a2b_hex(previous_output_value),
            int(status_code)
        )

        :param byte_string:
        :return: SHA512 Hash Class
        """

        return SHA512.new(
            byte_string
        )

    @classmethod
    def verify(cls, message_hash: SHA512Hash, signature: bytes) -> bool:
        """
        Verify a given NIST message hash and signature for a beacon value.

        :param message_hash:
            The hash that was carried out over the message.
            This is an object belonging to the `Crypto.Hash` module.
        :param signature: The signature that needs to be validated.
        :return: True if verification is correct. False otherwise.
        """

        return cls._verifier.verify(
            message_hash,
            signature,
        )
