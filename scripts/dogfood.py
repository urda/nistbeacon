#!/usr/bin/env python

import sys
from os.path import (
    abspath,
    dirname,
    join,
)

try:
    from nistbeacon import NistBeacon, NistBeaconValue
except ImportError:
    sys.path.insert(0, abspath(join(dirname(__file__), '..')))
    from nistbeacon import NistBeacon, NistBeaconValue


if __name__ == '__main__':
    print("Downloading records ...")

    target_timestamp = 1447873020
    records = {
        'get_record': NistBeacon.get_record(target_timestamp),
        'last_record': NistBeacon.get_last_record(),
        'next_record': NistBeacon.get_next(target_timestamp),
        'previous_record': NistBeacon.get_previous(target_timestamp),
    }

    for method_name, record in records.items():
        print("{0:.<30} ".format(method_name + " "), end="")

        if isinstance(record, NistBeaconValue):
            if record.valid_signature:
                print("[PASS]")
            else:
                print("[FAIL]")
                print("")
                print("Something is wonky with the signature verification!")
                print("")
                print("Please check:")
                print("   - The certificate")
                print("   - The certificate variables")
                print("   - NIST Service")
                print("   - NIST Documentation")
                sys.exit(1)
        else:
            print("[OFFLINE]")
            print("Got 'None', Beacon is offline or network issues exist.")
            sys.exit(2)

    sys.exit(0)
