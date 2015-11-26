#!/usr/bin/env python

from argparse import ArgumentParser
from os.path import (
    dirname,
    join,
)

curr_location = dirname(__file__)

paths = {
    'package': join(curr_location, '../py_nist_beacon/__init__.py'),
    'setup.py': join(curr_location, '../setup.py'),
}


class VersionScrapper(object):
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

    def scrape_version(self) -> str:
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


new_paths = [
    VersionScrapper(
        key_name='package',
        file_path=join(curr_location, '../py_nist_beacon/__init__.py'),
        magic_line="__version__ = '",
        strip_end_chars=1,
    ),
    VersionScrapper(
        key_name='setup.py',
        file_path=join(curr_location, '../setup.py'),
        magic_line="    version='",
        strip_end_chars=3,
    ),
]


def get_package_version() -> str:
    magic_line = "__version__ = '"

    try:
        f = open(paths['package'], 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            if magic_line in line:
                return line[len(magic_line):len(line)-1]

    except Exception as e:
        return str(e)


def get_setup_py_version() -> str:
    magic_line = "    version='"

    try:
        f = open(paths['setup.py'], 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            if magic_line in line:
                return line[len(magic_line):len(line)-3]

    except Exception as e:
        return str(e)


def get_versions() -> (bool, dict):

    versions_match = False
    versions = {}

    for version_obj in new_paths:
        versions[version_obj.key_name] = version_obj.scrape_version()

    return versions_match, versions


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
        _, data = get_versions()

        print(data)
