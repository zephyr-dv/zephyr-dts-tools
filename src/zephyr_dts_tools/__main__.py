'''
Created on Oct 5, 2021

@author: mballance
'''

import pcpp
import argparse
from .cmd_gen import gen as cmd_gen

def get_parser():
    parser = argparse.ArgumentParser()
    
    subparser = parser.add_subparsers()
    subparser.required = True
    subparser.dest="command"
    
    gen_cmd = subparser.add_parser("gen",
        help="generate files")
    gen_cmd.set_defaults(func=cmd_gen)

    gen_cmd.add_argument("-o", "--outdir",
        dest="outdir",
        help="Specifies the output directory")
    gen_cmd.add_argument("-d", "--dts-root", 
        help="Specifies a DTS_ROOT path",
        action="append", dest="dts_root")
    gen_cmd.add_argument("dts_file",
        help="Root Devicetree Specification file")
    gen_cmd.add_argument("template",
        help="Specifies a template directory or template id")
    
    return parser

def main():
    
    parser = get_parser()
    
    args = parser.parse_args()
    
    args.func(args)
    
    pass


if __name__ == "__main__":
    main()


