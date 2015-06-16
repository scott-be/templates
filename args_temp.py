#!/usr/bin/env python
import sys
import argparse

def main(argv):
    VERSION = '0.0'
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s v' + VERSION)
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-f', type=str, help="Input file name", dest="fname", metavar='FileName')
    group.add_argument('-p', type=str, help="Input path name", dest="path", metavar='PathName')

    args = parser.parse_args()
    if not (args.fname or args.path):
        parser.print_help()
        sys.exit()

    print(args.fname)
    print(args.path)

if __name__ == "__main__":
    main(sys.argv)