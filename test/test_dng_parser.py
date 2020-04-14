#!/usr/bin/env python

import argparse
import dng

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="dng parse tool")
    parser.add_argument("filename", help="dng file fullpath name")
    args = parser.parse_args()
    filename = args.filename

    dng = dng.DNGParser(filename)
    print(dng)
