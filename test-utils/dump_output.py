#!/usr/bin/python

from __future__ import absolute_import
from __future__ import print_function

import json
import sys

dumpFile=""
fileToGet=""
if len(sys.argv) > 2:
    dumpFile=sys.argv[1]
    fileToGet=sys.argv[2]
else:
    print ("Usage")
    print ("   dump_output.py <output.json> <file_to_dump>")
    exit (1)



file_lines=[l.strip("\n") for l in open(fileToGet, "r").readlines()]
output=json.loads(open(dumpFile).read())
output_files={}

if 'source_files' not in output:
    print ("output.json does not contain a 'source_files' array")
    print(output)
    exit (1)

for f in output['source_files']:
    output_files[f['name']] = f

if fileToGet not in output_files:
    print ("%s is not listed in %s" %(fileToGet, dumpFile))
    exit (1)

coverage=output_files[fileToGet]['coverage']

if len(coverage) != len(file_lines):
    print ("WARNING: Coverage reports %d lines, but file has %d"  %(len(coverage), len(file_lines)))

for i in range(len(file_lines)):
    hits = coverage[i]
    if hits == None:
        hits = "        "
    elif hits == 0:
        hits = "    MISS"
    else:
        hits = ("%8d" %hits)
    print ("%-5d %s:  %s" %(i+1, hits, file_lines[i]))
