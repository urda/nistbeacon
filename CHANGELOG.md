# Python NIST Randomness Beacon CHANGELOG

This is an alpha (pre-release) package. It's still in development, but has
basic functionality fleshed out. Please refer to the `README` of the
project to get started.

- [PyPI - py_nist_beacon](https://pypi.python.org/pypi/py_nist_beacon/)

## v0.7.0 (Alpha Release)

Name change due to _ vs - ? Maybe.

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
