#!/usr/bin/env python

# Merge two json files into one. If there is a conflict in the files B's values will always be used.

from optparse import OptionParser
import json
import sys

parser = OptionParser()

# Setup options for the parser
parser.add_option("-a", dest="a",
                  help="One file to merge")

parser.add_option("-b", dest="b",
                  help="The other file to merge")

parser.add_option("-f", "--file", dest="filename",
                  help="The resulting file", metavar="FILE")

(options, args) = parser.parse_args()

if not options.a:
    print >> sys.stderr, "File A is required"
    exit(1)

if not options.b:
    print >> sys.stderr, "File B is required"
    exit(1)

if not options.filename:
    print >> sys.stderr, "File output is required"
    exit(1)

file_a = open(options.a, 'r')
file_a_data = json.load(file_a)
file_a.close()

file_b = open(options.b, 'r')
file_b_data = json.load(file_b)
file_b.close()

file_a_data.update(file_b_data)

combined_data = file_a_data

f = open(options.filename, 'w')
f.write(json.dumps(combined_data))
f.close()