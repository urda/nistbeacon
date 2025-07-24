## v1 to v2 Notes

### NIST Beacon v1 to v2 Migration Plan

#### API Endpoint Changes

- Update the base URL in `NistBeacon._NIST_API_URL` from `https://beacon.nist.gov/rest/record` to `https://beacon.nist.gov/beacon/2.0`
- Modify the URL path construction in `_query_nist()` method to match v2 API paths (e.g., `/pulse/last` instead of `/last`)
- Add support for chain selection (v2 supports multiple chains with different IDs)

#### Data Structure Updates

- Rename `NistBeaconValue` class to `NistBeaconPulse` (or create a new class) to reflect v2 terminology
- Add new required fields to the pulse class:
  - `uri` - URI of the pulse
  - `version` - Version string (will be "Version 2.0")
  - `chainIndex` - Chain index number
  - `pulseIndex` - Pulse index within the chain
  - `localRandomValue` - Local random value
  - `external` - External input sources object
  - `listValues` - List of values from external sources
  - `certificateId` - ID of the certificate used for signing

#### XML Parsing Updates

- Update XML namespace in `from_xml()` method from `http://beacon.nist.gov/record/0.1/` to `https://beacon.nist.gov/beacon/2.0/`
- Update XML template string to match v2 format with new fields
- Modify parsing logic to handle nested elements (v2 has a more complex structure)

#### Cryptographic Verification Updates

- Add new certificates and public keys for v2 chains in `NistBeaconCrypto`
- Update the `get_hash()` method to handle v2's different hashing approach
- Modify the `verify()` method to support v2's signature verification process
- Update timestamp-based verifier selection logic to include v2 certificates

#### New Features to Implement

- Add support for retrieving chain information (`/chains` endpoint)
- Implement methods to get pulses by chain index and pulse index
- Add support for retrieving combinations of pulses
- Implement methods to access external source values

#### Backward Compatibility

- Consider maintaining v1 API support alongside v2
- Add version parameter to methods that can work with both APIs
- Create adapter/wrapper classes to maintain compatibility with existing code

#### Testing and Validation

- Create tests for v2 API endpoints
- Validate signature verification with known-good v2 pulses
- Test chain traversal and pulse retrieval
- Verify handling of different status codes

#### Documentation Updates

- Update class and method documentation to reflect v2 terminology
- Document new methods and parameters
- Add examples for working with v2-specific features
- Update README with migration guide for users

#### Implementation Strategy

1. Start by creating new classes for v2 (don't modify existing ones yet)
2. Implement basic pulse retrieval and parsing
3. Add cryptographic verification
4. Implement chain-specific functionality
5. Add backward compatibility layer
6. Update tests and documentation
