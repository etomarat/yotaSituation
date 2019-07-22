#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""yotaSituation commandline interface"""

import argparse
import importlib

requests = importlib.import_module('requests')

parser = argparse.ArgumentParser(description='Get info from Yota modem')
parser.add_argument('commands', metavar='N', type=str, nargs='*', 
                    default=['GeneralInfo'], choices=[['GeneralInfo'], 'GeneralInfo', 'Status'],
                    help='Commands names to run. Available: %(choices)s, default: %(default)s')
args = parser.parse_args()

if __name__ == "__main__":
  for command in args.commands:
    print 'command %s result:' % command
    class_ = getattr(requests, command)
    print class_()
