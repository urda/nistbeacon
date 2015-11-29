#!/usr/bin/env python


import sys
from argparse import ArgumentParser
from os.path import (
    abspath,
    dirname,
    join,
)

try:
    from py_nist_beacon import NistRandomnessBeacon
except ImportError:
    sys.path.insert(0, abspath(join(dirname(__file__), '..')))
    from py_nist_beacon import NistRandomnessBeacon


if __name__ == '__main__':
    # Parse arguments
    parser = ArgumentParser()

    parser.add_argument(
        "--debug",
        help="show 'DEBUG' statements",
        action="store_true",
    )

    args = parser.parse_args()
    debug = args.debug

    print("Downloading records ...")

    target_timestamp = 1447873020
    records = {
        'get_record': NistRandomnessBeacon.get_record(target_timestamp),
        'last_record': NistRandomnessBeacon.get_last_record(),
        'next_record': NistRandomnessBeacon.get_next(target_timestamp),
        'previous_record': NistRandomnessBeacon.get_previous(target_timestamp),
    }

    if debug:
        for method_name, record in records.items():
            print(method_name)
            print(record.to_json())
            print("")

    for method_name, record in records.items():
        print("{0:.<30} ".format(method_name + " "), end="")

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

    sys.exit(0)
