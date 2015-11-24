from xml.etree import ElementTree

import py_nist_beacon.nist_beacon_constants as cn


class NistRandomnessBeaconValue(object):
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
            frequency, timeStamp, seedValue, previousHashValue, errorCode

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

        self.version = version
        self.frequency = frequency
        self.timestamp = timestamp
        self.seed_value = seed_value
        self.previous_output_value = previous_output_value
        self.signature_value = signature_value
        self.output_value = output_value
        self.status_code = status_code

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
