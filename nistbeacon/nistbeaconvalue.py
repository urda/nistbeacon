"""
Copyright 2015-2020 Peter Urda

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
import hashlib
import json
from random import Random
from typing import Optional
from xml.etree import ElementTree

from nistbeacon.nistbeaconcrypto import NistBeaconCrypto


class NistBeaconValue:
    """
    A single NIST Beacon Value object represents one beacon value.
    It has all the normal properties of a NIST beacon API call,
    but stored as a python object
    """

    _xml_template = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<record xmlns="http://beacon.nist.gov/record/0.1/">'
        '<version>{0}</version>'
        '<frequency>{1}</frequency>'
        '<timeStamp>{2}</timeStamp>'
        '<seedValue>{3}</seedValue>'
        '<previousOutputValue>{4}</previousOutputValue>'
        '<signatureValue>{5}</signatureValue>'
        '<outputValue>{6}</outputValue>'
        '<statusCode>{7}</statusCode>'
        '</record>'
    )

    _KEY_FREQUENCY = 'frequency'
    _KEY_OUTPUT_VALUE = 'outputValue'
    _KEY_PREVIOUS_OUTPUT_VALUE = 'previousOutputValue'
    _KEY_SEED_VALUE = 'seedValue'
    _KEY_SIGNATURE_VALUE = 'signatureValue'
    _KEY_STATUS_CODE = 'statusCode'
    _KEY_TIMESTAMP = 'timeStamp'
    _KEY_VERSION = 'version'

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

        # Compute JSON, XML strings
        self._json = json.dumps(
            {
                self._KEY_VERSION: self.version,
                self._KEY_FREQUENCY: self.frequency,
                self._KEY_TIMESTAMP: self.timestamp,
                self._KEY_SEED_VALUE: self.seed_value,
                self._KEY_PREVIOUS_OUTPUT_VALUE: self.previous_output_value,
                self._KEY_SIGNATURE_VALUE: self.signature_value,
                self._KEY_OUTPUT_VALUE: self.output_value,
                self._KEY_STATUS_CODE: self.status_code,
            },
            sort_keys=True,
        )

        self._xml = self._xml_template.format(
            self.version,
            self.frequency,
            self.timestamp,
            self.seed_value,
            self.previous_output_value,
            self.signature_value,
            self.output_value,
            self.status_code,
        )

        # Signature checking
        sha512_hash = NistBeaconCrypto.get_hash(
            self.version,
            self.frequency,
            self.timestamp,
            self.seed_value,
            self.previous_output_value,
            self.status_code,
        )

        sig_check_result = NistBeaconCrypto.verify(
            timestamp=self.timestamp,
            message_hash=sha512_hash,
            signature=binascii.a2b_hex(self.signature_value)[::-1],
        )

        # The signature sha512'd again should equal the output value
        expected_signature = hashlib.sha512(
            binascii.a2b_hex(self.signature_value)
        ).hexdigest().upper()

        sig_hash_check = expected_signature == self.output_value

        # Store the valid signature state after computation
        self._valid_signature = sig_check_result and sig_hash_check

        # Using the output value from the beacon, let's seed a personal
        # python random.Random object
        self._pseudo_random = Random(self.output_value)

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
    def json(self) -> str:
        """
        :return: The JSON representation of the beacon, as a string
        """

        return self._json

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
    def pseudo_random(self) -> Random:
        """
        :return:
            A python `random.Random` object that has been seeded with
            the value's `output_value`. This is a pseudo-random
            number generator
        """

        return self._pseudo_random

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

    @property
    def xml(self) -> str:
        """
        :return: The XML representation of the beacon, as a string
        """

        return self._xml

    @classmethod
    def from_json(cls, input_json: str) -> 'NistBeaconValue':
        """
        Convert a string of JSON which represents a NIST randomness beacon
        value into a 'NistBeaconValue' object.

        :param input_json: JSON to build a 'Nist RandomnessBeaconValue' from
        :return: A 'NistBeaconValue' object, 'None' otherwise
        """

        try:
            data_dict = json.loads(input_json)
        except ValueError:
            return None

        # Our required values are "must haves". This makes it simple
        # to verify we loaded everything out of JSON correctly.
        required_values = {
            cls._KEY_FREQUENCY: None,
            cls._KEY_OUTPUT_VALUE: None,
            cls._KEY_PREVIOUS_OUTPUT_VALUE: None,
            cls._KEY_SEED_VALUE: None,
            cls._KEY_SIGNATURE_VALUE: None,
            cls._KEY_STATUS_CODE: None,
            cls._KEY_TIMESTAMP: None,
            cls._KEY_VERSION: None,
        }

        for key in required_values:
            if key in data_dict:
                required_values[key] = data_dict[key]

        # Confirm that the required values are set, and not 'None'
        if None in required_values.values():
            return None

        # We have all the required values, return a node object
        return cls(
            version=required_values[cls._KEY_VERSION],
            frequency=int(required_values[cls._KEY_FREQUENCY]),
            timestamp=int(required_values[cls._KEY_TIMESTAMP]),
            seed_value=required_values[cls._KEY_SEED_VALUE],
            previous_output_value=required_values[
                cls._KEY_PREVIOUS_OUTPUT_VALUE
            ],
            signature_value=required_values[cls._KEY_SIGNATURE_VALUE],
            output_value=required_values[cls._KEY_OUTPUT_VALUE],
            status_code=required_values[cls._KEY_STATUS_CODE],
        )

    @classmethod
    def from_xml(cls, input_xml: str) -> Optional['NistBeaconValue']:
        """
        Convert a string of XML which represents a NIST Randomness Beacon value
        into a 'NistBeaconValue' object.

        :param input_xml: XML to build a 'NistBeaconValue' from
        :return: A 'NistBeaconValue' object, 'None' otherwise
        """

        invalid_result = None

        understood_namespaces = {
            'nist-0.1': 'http://beacon.nist.gov/record/0.1/',
        }

        # Our required values are "must haves". This makes it simple
        # to verify we loaded everything out of XML correctly.
        required_values = {
            cls._KEY_FREQUENCY: None,
            cls._KEY_OUTPUT_VALUE: None,
            cls._KEY_PREVIOUS_OUTPUT_VALUE: None,
            cls._KEY_SEED_VALUE: None,
            cls._KEY_SIGNATURE_VALUE: None,
            cls._KEY_STATUS_CODE: None,
            cls._KEY_TIMESTAMP: None,
            cls._KEY_VERSION: None,
        }

        # First attempt to load the xml, return 'None' on ParseError
        try:
            tree = ElementTree.ElementTree(ElementTree.fromstring(input_xml))
        except ElementTree.ParseError:
            return invalid_result

        # Using the required values, let's load the xml values in
        for key in required_values:
            discovered_element = tree.find(
                f'nist-0.1:{key}',
                namespaces=understood_namespaces,
            )

            if not isinstance(discovered_element, ElementTree.Element):
                continue

            # Bad pylint message - https://github.com/PyCQA/pylint/issues/476
            # pylint: disable=no-member
            required_values[key] = discovered_element.text

        # Confirm that the required values are set, and not 'None'
        if None in required_values.values():
            return invalid_result

        # We have all the required values, return a node object
        return cls(
            version=required_values[cls._KEY_VERSION],
            frequency=int(required_values[cls._KEY_FREQUENCY]),
            timestamp=int(required_values[cls._KEY_TIMESTAMP]),
            seed_value=required_values[cls._KEY_SEED_VALUE],
            previous_output_value=required_values[
                cls._KEY_PREVIOUS_OUTPUT_VALUE
            ],
            signature_value=required_values[cls._KEY_SIGNATURE_VALUE],
            output_value=required_values[cls._KEY_OUTPUT_VALUE],
            status_code=required_values[cls._KEY_STATUS_CODE],
        )
