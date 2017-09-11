# Python NIST Randomness Beacon CHANGELOG

## v0.9.3 (Beta Release)

- Updated README links for Codecov
- Updated library to use additional signing key
  - For more details, see:
    - https://github.com/urda/nistbeacon/issues/22
    - https://github.com/urda/nistbeacon/issues/26

## v0.9.2 (Beta Release)

- Internal Changes
  - LICENSE
    - Updated for 2016.
  - `NistBeacon`
    - `get_first_record` now defaults to downloading the first record.
  - `NistBeaconCrypto`
    - Now computes the `struct` and other values for the `SHA512Hash`.
  - `NistBeaconValue`
    - Pushed `struct` and signature hash building into
      `NistBeaconCrypto`.
- Project Changes
  - Coverage Tool
    - Switched from Coveralls to Codecov.

## v0.9.1 (Beta Release)

- Internal Changes
  - `NistBeacon`
    - `NIST_BASE_URL` renamed to `_NIST_API_URL`, to clarify that the value
      should **NOT** be altered under normal circumstances.
  - `NistBeaconCrypto`
    - New helper class for signature checking of `NistBeaconValue` objects.
      This is **NOT** a class designed for general use!
  - `NistBeaconValue`
    - Added a helper class `NistBeaconCrypto` to handle SHA512 generation
      and signature checking. This means that `NistBeaconCrypto` needs to
      be the only reference for key import and signature checking. All
      other `NistBeaconValue` do not have to generate the full RSA objects.
    - Started using the now existing `xmlns` property directly from NIST.

## v0.9.0 (Beta Release)

- Features
  - `NistBeaconValue`
    - Added a `pseudo_random` property.
      Returns a `random.Random` object that has been seeded with
      the `output_value` for a given `NistBeaconValue`.

## v0.8.3 (Alpha Release)

- Internal Changes
  - `NistBeaconValue`
    - Creating a beacon value will store the JSON, XML representations once.
      These values do not have to be computed on each `json` or `xml` property
      access now as before.
- Project Changes (for Developers)
  - `pylint` has been added to the project and build process.

## v0.8.2 (Alpha Release, Bug Fix)

- Bug Fixes:
  - `NistBeaconValue`
    - Reported issue where a `xmlns` value on `record` ended up breaking XML loading.
      Reported on [GitHub](https://github.com/urda/nistbeacon/issues/8). Since this
      is just a bug fix release. This `xmlns` value will not show up if one was to
      use the `xml` value from the `NistBeaconValue` object.

## v0.8.1 (Alpha Release)

- Minor documentation changes

## v0.8.0 (Alpha Release)

- Features
  - `NistBeaconValue`
    - Added `json` and `xml` as properties (replaces `to_json()` and `to_xml()`)

## v0.7.0 (Alpha Release)

- Name changes
  - Changed from `py_nist_beacon` to `nistbeacon`
  - Changed from `NistRandomnessBeacon` to `NistBeacon`
  - Changed from `NistRandomnessBeaconValue` to `NistBeaconValue`

## v0.6.0 (Alpha Release)

- Features
  - `NistRandomnessBeacon`
    - Added a `get_first_record` method. An optional boolean flag named
      `download` allows the caller to either use the local first record
      object, or to download the first record directly from the NIST beacon.

## v0.5.2 (Alpha Release)

- Added a section on installation.
- Updated `CONTRIBUTING`
- Re-do `PHONY` targets in `Makefile`
- Update `travis` build steps to include `3.5-dev` and `nightly`

## v0.5.1 (Alpha Release)

- Badges made to point to their release branches

## v0.5.0 (Alpha Release)

- General
  - Lots of documentation added through `docstrings`! :memo:
- `NistRandomnessBeacon`
  - The beacon now understands how to check the chain. Using the `chain_check`
    method on the beacon with a given `timestamp` value the NIST Randomness
    Beacon chain can be verified for integrity purposes. :link:

```python
@classmethod
def chain_check(cls, timestamp: int) -> bool:
    """
    Given a record timestamp, verify the chain integrity.

    :param timestamp: UNIX time / POSIX time / Epoch time
    :return: 'True' if the timestamp fits the chain. 'False' otherwise.
    """
```

- `NistRandomnessBeaconValue`
  - :warning: All properties of the beacon have been placed behind `@property`
    decorators to minimize possible manipulation
  - :warning:  `verify_signature` has been removed from beacon values.
    **Replaced with `valid_signature`**
  - Introduced `valid_signature` as a `bool` property.
    **Replaces `verify_signature`**

## v0.4.0 (Alpha Release)

- Added a `verify_signature` to `NistRandomnessBeaconValue` objects.
  This method returns a `True` or `False` after verifying the provided
  record. The record is verified using two steps:
  - First, using a combination of input data of the record, a simple message
    is packed to create a message. That message is then used in combination with
    the record's reported `signature_value` and the **known**
    [NIST Beacon X.509 certificate](https://beacon.nist.gov/certificate/beacon.cer).
    This certificate is available for download, but is baked into the application
    as follows:
    - Original CER file as a string: `nist_beacon_constants.py - NIST_CER_FILE`
    - Original Public Key as a string: `nist_beacon_constants.py - NIST_RSA_KEY`
    - Hard copy of `beacon.cer` is provided at the root of the project
  - Second, the `signature_value` is ran through a `sha512` hash to confirm the
    `output_value` is correct on the record.
  - If either of the steps are found to be invalid, `verify_signature` will
    return a `False` result.

## v0.3.0 (Alpha Release)

- Added `to_xml`, `to_json`, and `from_json` methods on beacon values

## v0.2.0 (Alpha Release)

- Initial PyPI release package
