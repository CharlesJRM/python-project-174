#!/usr/bin/env python3
import argparse
import sys
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", default="stylish",
        help="set format of output (stylish, plain, json)"
    )
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    sys.exit(main())
