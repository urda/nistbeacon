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
