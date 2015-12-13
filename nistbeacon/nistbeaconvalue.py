import binascii
import hashlib
import json
import struct
from xml.etree import ElementTree

from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import nistbeacon.constants as cn


class NistBeaconValue(object):
    def __init__(
            self,
            version: str,
            frequency: int,
            timestamp: int,
            seed_value: str,
            previous_output_value: str,
            signature_value: str,
            output_value: str,
            status_code: str,
    ):
        """
        :param version:
            Reported NIST randomness beacon version

        :param frequency:
            The time interval, in seconds, between expected records

        :param timestamp:
            The time the seed value was generated as the number of
            seconds since January 1, 1970

        :param seed_value:
            A seed value represented as a 64 byte (512-bit) hex string
            value

        :param previous_output_value:
            The SHA-512 hash value for the previous record - 64 byte hex
            string

        :param signature_value:
            A digital signature (RSA) computed over (in order): version,
            frequency, timeStamp, seedValue, previousHashValue, statusCode

            Note: Except for version, the hash is on the byte
            representations and not the string representations of the data
            values

        :param output_value:
            The SHA-512 hash of the signatureValue as a 64 byte hex string

        :param status_code:
            The status code value:
                0 - Chain intact, values all good
                1 - Start of a new chain of values, previous hash value
                    will be all zeroes
                2 - Time between values is greater than the frequency, but
                    the chain is still intact
        """

        self._version = version
        self._frequency = frequency
        self._timestamp = timestamp
        self._seed_value = seed_value
        self._previous_output_value = previous_output_value
        self._signature_value = signature_value
        self._output_value = output_value
        self._status_code = status_code

        # Internal properties
        self._rsa_signature = binascii.a2b_hex(self.signature_value)[::-1]

        self._rsa_message = SHA512.new(
            self.version.encode() +
            struct.pack(
                '>1I1Q64s64s1I',
                self.frequency,
                self.timestamp,
                binascii.a2b_hex(self.seed_value),
                binascii.a2b_hex(self.previous_output_value),
                int(self.status_code)
            )
        )

        # Get the RSA key, and build a verifier with it
        rsa_key = RSA.importKey(cn.NIST_RSA_KEY)
        verifier = PKCS1_v1_5.new(rsa_key)

        # Check the message against the signature
        if verifier.verify(self._rsa_message, self._rsa_signature):
            sig_check_result = True
        else:
            sig_check_result = False

        # The signature sha512'd again should equal the output value
        expected_signature = hashlib.sha512(
            binascii.a2b_hex(self.signature_value)
        ).hexdigest().upper()

        sig_hash_check = (expected_signature == self.output_value)

        self._valid_signature = sig_check_result and sig_hash_check

    def __eq__(self, other):
        try:
            return self.version == other.version \
                   and self.frequency == other.frequency \
                   and self.timestamp == other.timestamp \
                   and self.seed_value == other.seed_value \
                   and self.previous_output_value == \
                   other.previous_output_value \
                   and self.signature_value == other.signature_value \
                   and self.output_value == other.output_value \
                   and self.status_code == other.status_code \
                   and self.valid_signature == other.valid_signature
        except (AttributeError, TypeError):
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def frequency(self) -> int:
        """
        :return: The time interval, in seconds, between expected records
        """

        return self._frequency

    @property
    def output_value(self) -> str:
        """
        :return: The SHA-512 hash of the signatureValue as a 64 byte hex string
        """

        return self._output_value

    @property
    def previous_output_value(self) -> str:
        """
        :return:
            The SHA-512 hash value for the previous record - 64 byte hex
            string
        """

        return self._previous_output_value

    @property
    def seed_value(self) -> str:
        """
        :return:
            A seed value represented as a 64 byte (512-bit) hex string
            value
        """

        return self._seed_value

    @property
    def signature_value(self) -> str:
        """
        :return:
            A digital signature (RSA) computed over (in order): version,
            frequency, timeStamp, seedValue, previousHashValue, statusCode

            Note: Except for version, the hash is on the byte
            representations and not the string representations of the data
            values
        """

        return self._signature_value

    @property
    def status_code(self) -> str:
        """
        :return:
            The status code value:
                0 - Chain intact, values all good
                1 - Start of a new chain of values, previous hash value
                    will be all zeroes
                2 - Time between values is greater than the frequency, but
                    the chain is still intact
        """

        return self._status_code

    @property
    def timestamp(self) -> int:
        """
        :return:
            The time the seed value was generated as the number of
            seconds since January 1, 1970
        """

        return self._timestamp

    @property
    def valid_signature(self) -> bool:
        """
        Shows the result of signature verification

        First, required records (version, frequency, timestamp,
        seed_value, previous_output_value) are packed together to form
        a message. This message is then checked against the record's reported
        signature field WITH the known NIST public key.

        Second, the signature value is independently ran through a SHA512
        hash. The result of this operation SHOULD equal the record's reported
        output_value field.

        As long as the result of the 'First' step and'ed with the 'Second'
        step, the record is considered valid.

        :return: 'True' if this record is valid. 'False' otherwise
        """

        return self._valid_signature

    @property
    def version(self) -> str:
        """
        :return: Reported NIST randomness beacon version
        """

        return self._version

    @classmethod
    def from_json(cls, input_json: str):
        """
        Convert a string of JSON which represents a NIST randomness beacon
        value into a 'NistRandomnessBeaconValue' object.

        :param input_json: JSON to build a 'Nist RandomnessBeaconValue' from
        :return: A 'NistRandomnessBeaconValue' object, 'None' otherwise
        """

        try:
            data_dict = json.loads(input_json)
        except ValueError:
            return None

        # Our required values are "must haves". This makes it simple
        # to verify we loaded everything out of JSON correctly.
        required_values = {
            cn.NIST_KEY_FREQUENCY: None,
            cn.NIST_KEY_OUTPUT_VALUE: None,
            cn.NIST_KEY_PREVIOUS_OUTPUT_VALUE: None,
            cn.NIST_KEY_SEED_VALUE: None,
            cn.NIST_KEY_SIGNATURE_VALUE: None,
            cn.NIST_KEY_STATUS_CODE: None,
            cn.NIST_KEY_TIMESTAMP: None,
            cn.NIST_KEY_VERSION: None,
        }

        for key in required_values:
            if key in data_dict:
                required_values[key] = data_dict[key]

        # Confirm that the required values are set, and not 'None'
        if None in required_values.values():
            return None

        # We have all the required values, return a node object
        return cls(
            version=required_values[cn.NIST_KEY_VERSION],
            frequency=int(required_values[cn.NIST_KEY_FREQUENCY]),
            timestamp=int(required_values[cn.NIST_KEY_TIMESTAMP]),
            seed_value=required_values[cn.NIST_KEY_SEED_VALUE],
            previous_output_value=required_values[
                cn.NIST_KEY_PREVIOUS_OUTPUT_VALUE
            ],
            signature_value=required_values[cn.NIST_KEY_SIGNATURE_VALUE],
            output_value=required_values[cn.NIST_KEY_OUTPUT_VALUE],
            status_code=required_values[cn.NIST_KEY_STATUS_CODE],
        )

    def to_json(self) -> str:
        """
        Convert the given NIST randomness beacon value to JSON

        :return: The JSON representation of the beacon, as a string
        """

        return json.dumps(
            {
                cn.NIST_KEY_VERSION: self.version,
                cn.NIST_KEY_FREQUENCY: self.frequency,
                cn.NIST_KEY_TIMESTAMP: self.timestamp,
                cn.NIST_KEY_SEED_VALUE: self.seed_value,
                cn.NIST_KEY_PREVIOUS_OUTPUT_VALUE: self.previous_output_value,
                cn.NIST_KEY_SIGNATURE_VALUE: self.signature_value,
                cn.NIST_KEY_OUTPUT_VALUE: self.output_value,
                cn.NIST_KEY_STATUS_CODE: self.status_code,
            },
            sort_keys=True,
        )

    @classmethod
    def from_xml(cls, input_xml: str):
        """
        Convert a string of XML which represents a NIST Randomness Beacon value
        into a 'NistRandomnessBeaconValue' object.

        :param input_xml: XML to build a 'NistRandomnessBeaconValue' from
        :return: A 'NistRandomnessBeaconValue' object, 'None' otherwise
        """

        invalid_result = None

        # Our required values are "must haves". This makes it simple
        # to verify we loaded everything out of XML correctly.
        required_values = {
            cn.NIST_KEY_FREQUENCY: None,
            cn.NIST_KEY_OUTPUT_VALUE: None,
            cn.NIST_KEY_PREVIOUS_OUTPUT_VALUE: None,
            cn.NIST_KEY_SEED_VALUE: None,
            cn.NIST_KEY_SIGNATURE_VALUE: None,
            cn.NIST_KEY_STATUS_CODE: None,
            cn.NIST_KEY_TIMESTAMP: None,
            cn.NIST_KEY_VERSION: None,
        }

        # First attempt to load the xml, return 'None' on ParseError
        try:
            tree = ElementTree.fromstring(input_xml)
        except ElementTree.ParseError:
            return invalid_result

        # Using the required values, let's load the xml values in
        for key in required_values:
            discovered_element = tree.find(key)

            if discovered_element is None:
                continue

            required_values[key] = discovered_element.text

        # Confirm that the required values are set, and not 'None'
        if None in required_values.values():
            return invalid_result

        # We have all the required values, return a node object
        return cls(
            version=required_values[cn.NIST_KEY_VERSION],
            frequency=int(required_values[cn.NIST_KEY_FREQUENCY]),
            timestamp=int(required_values[cn.NIST_KEY_TIMESTAMP]),
            seed_value=required_values[cn.NIST_KEY_SEED_VALUE],
            previous_output_value=required_values[
                cn.NIST_KEY_PREVIOUS_OUTPUT_VALUE
            ],
            signature_value=required_values[cn.NIST_KEY_SIGNATURE_VALUE],
            output_value=required_values[cn.NIST_KEY_OUTPUT_VALUE],
            status_code=required_values[cn.NIST_KEY_STATUS_CODE],
        )

    def to_xml(self) -> str:
        """
        Convert the given NIST randomness beacon value back to XML

        :return: The XML representation of the beacon, as a string
        """

        return cn.NIST_XML_TEMPLATE.format(
            self.version,
            self.frequency,
            self.timestamp,
            self.seed_value,
            self.previous_output_value,
            self.signature_value,
            self.output_value,
            self.status_code,
        )
