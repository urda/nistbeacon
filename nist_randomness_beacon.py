#! /usr/bin/env python

NIST_BASE_URL = "https://beacon.nist.gov/rest/record"


class nist_beacon_value(object):
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

            self.version = None
            self.frequency = None
            self.timestamp = None
            self.seed_value = None
            self.previous_output_value = None
            self.signature_value = None
            self.output_value = None
            self.status_code = None


if __name__ == '__main__':
    pass
