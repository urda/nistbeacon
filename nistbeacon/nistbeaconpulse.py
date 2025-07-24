"""
Copyright 2025 Peter Urda

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


class NistBeaconPulse:
    """
    NIST Beacon Pulse

    Version 2.0 of the pulse format has become more complex,
    compared to the version (1) used in the initial NIST beacon prototype.
    Some of the new complexity intends to make operating a beacon easier.
    Other parts intend to improve the security against a misbehaving beacon.
    Still others intend to make it easier to securely combine outputs from
    different beacons.
    """

    _DEFAULT_VERSION = ''

    _KEY_URI = 'uri'
    _KEY_VERSION = 'version'
    _KEY_CIPHER_SUITE = 'cipherSuite'
    _KEY_PERIOD = 'period'
    _KEY_CERTIFICATE_ID = 'certificateId'
    _KEY_CHAIN_INDEX = 'chainIndex'
    _KEY_PULSE_INDEX = 'pulseIndex'
    _KEY_TIME_STAMP = 'timeStamp'
    _KEY_LOCAL_RANDOM_VALUE = 'localRandomValue'
    _KEY_EXTERNAL = 'external'
    _KEY_EXTERNAL_SOURCE_ID = 'sourceId'
    _KEY_EXTERNAL_STATUS_CODE = 'statusCode'
    _KEY_EXTERNAL_VALUE = 'value'
    _KEY_LIST_VALUE_URI = 'uri'
    _KEY_LIST_VALUE_TYPE = 'type'
    _KEY_LIST_VALUE_VALUE = 'value'
    _KEY_PRECOMMITMENT_VALUE = 'precommitmentValue'
    _KEY_STATUS_CODE = 'statusCode'
    _KEY_SIGNATURE_VALUE = 'signatureValue'
    _KEY_OUTPUT_VALUE = 'outputValue'

    _version: str

    def __init__(
            self,
            version: str = 'Version 2.0',
    ):
        """
        :param version:
            Reported NIST randomness beacon version
        """
        self._version = version

        self._verify_props()

    @property
    def version(self) -> str:
        return self._version

    def _verify_props(self) -> None:
        if not self._version:
            raise ValueError('Version cannot be null.')
