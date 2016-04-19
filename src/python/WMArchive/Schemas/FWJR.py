#!/usr/bin/env python
#-*- coding: utf-8 -*-
#pylint: disable=
"""
File       : FWJR.py
Author     : Valentin Kuznetsov <vkuznet AT gmail dot com>
Description: FWJR schema manager
"""

# system modules
import os
import sys
import time
import json
import pprint
import argparse

# WMArchive modules
from WMArchive.Schemas.FWJRProduction import fwjr as fwjr_prod
from WMArchive.Schemas.FWJRTest import fwjr as fwjr_test

def schema(stype, fout):
    "Write out schema of given type into provided output file name"
    if  stype == 'production':
        fwjr = fwjr_prod
    elif stype == 'test':
        fwjr = fwjr_test
    else:
        raise NotImplementedError
    # use default values for schema, WMArchive will put real values later
    fwjr['wmaid'] = ''
    fwjr['wmats'] = 0.
    fwjr['stype'] = ''
    if  fout:
        with open(fout, 'w') as ostream:
            ostream.write(json.dumps(fwjr))
    else:
        pprint.pprint(fwjr)

class OptionParser():
    def __init__(self):
        "User based option parser"
        self.parser = argparse.ArgumentParser(prog='PROG')
        self.parser.add_argument("--schema", action="store",
            dest="schema", default="production", help="Specify schema type, production or test")
        self.parser.add_argument("--fout", action="store",
            dest="fout", default="", help="Specify output file name")

def main():
    "Main function"
    optmgr  = OptionParser()
    opts = optmgr.parser.parse_args()
    schema(opts.schema, opts.fout)

if __name__ == '__main__':
    main()
