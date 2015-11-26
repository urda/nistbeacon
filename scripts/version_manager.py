#!/usr/bin/env python

import sys
from argparse import ArgumentParser
from collections import Counter
from os.path import (
    dirname,
    join,
)


class FileVersionInfo(object):
    def __init__(
            self,
            key_name: str,
            file_path: str,
            magic_line: str,
            strip_end_chars: int = 0,
    ):
        self.key_name = key_name
        self.file_path = file_path
        self.magic_line = magic_line
        self.strip_end_chars = strip_end_chars

    def get_version(self) -> str:
        try:
            f = open(self.file_path, 'r')
            lines = f.readlines()
            f.close()
        except Exception as e:
            return str(e)

        result = ''

        for line in lines:
            if self.magic_line in line:
                start = len(self.magic_line)
                end = len(line) - self.strip_end_chars
                result = line[start:end]
                break

        return result


class FileVersionResult(object):
    def __init__(
            self,
            uniform: bool,
            version_details: dict,
            version_result: str
    ):
        self.uniform = uniform
        self.version_details = version_details
        self.version_result = version_result


curr_location = dirname(__file__)
version_objects = [
    FileVersionInfo(
        key_name='package',
        file_path=join(curr_location, '../py_nist_beacon/__init__.py'),
        magic_line="__version__ = '",
        strip_end_chars=2,
    ),
    FileVersionInfo(
        key_name='setup.py',
        file_path=join(curr_location, '../setup.py'),
        magic_line="    version='",
        strip_end_chars=3,
    ),
]


def get_versions() -> FileVersionResult:

    version_counter = Counter()
    versions_match = False
    version_str = None
    versions_discovered = {}

    for version_obj in version_objects:
        discovered = version_obj.get_version()
        versions_discovered[version_obj.key_name] = discovered
        version_counter.update([discovered])

    if len(version_counter) == 1:
        versions_match = True
        version_str = list(version_counter.keys())[0]

    return FileVersionResult(
        uniform=versions_match,
        version_details=versions_discovered,
        version_result=version_str,
    )


if __name__ == '__main__':

    parser = ArgumentParser()

    understood_commands = [
        'check',
    ]

    sp = parser.add_subparsers(dest="command")
    for command in understood_commands:
        sp.add_parser(command)

    args = parser.parse_args()

    if args.command == "check":
        version_data = get_versions()

        if version_data.uniform:
            print("Versions look OK across the project")
            print("Version: '{}'".format(version_data.version_result))
        else:
            print("Versions DO NOT MATCH across the project!")
            print()
            for key, version_val in version_data.version_details.items():
                print("{0: <10}: {1}".format(key, version_val))

            sys.exit(1)

    sys.exit(0)
