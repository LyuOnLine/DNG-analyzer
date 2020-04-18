#!/usr/bin/env python

import sys
import os
sys.path.append(os.getcwd())
import argparse
import dng
import IPython


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="dng parse tool")
    parser.add_argument('-i', "--interactive",
                        dest="interactive", action="store_true")
    parser.add_argument("filename", help="dng file fullpath name")
    args = parser.parse_args()
    filename = args.filename

    dng = dng.DNGParser(filename)
    print(dng)
    if args.interactive:
        IPython.embed(banner1="dng analyzer started.",
                      banner2="\tdng.ifd0.TAGNAME: show detail tag info of ifd0\n\tdng.subifd0[0].TAGNAME: show detail tag info of subifds")
