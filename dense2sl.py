#!/usr/bin/env python2.6
from __future__ import print_function
import sys

base = sys.argv[1]
base = int(base)
print("starting index = %d" % base,  file=sys.stderr)

for line in sys.stdin:
  parts = line.split()
  gen = ("%d:%s" % (j+base,val) for j,val in enumerate(parts))
  print(*gen)
