#!/usr/bin/env python2.6
""" 
input: 1-indexed i,j,val coordinate-format triples.  (matlab-compatible)
output: svmlight/libsvm-style right side of lines, the j:val format.
This only handles the feature matrix 'X'.  use 'paste' to combine this output with labels. """
from __future__ import print_function
import os,sys


cur_i = 1

for line in sys.stdin:
  i,j,val = line.split()
  i=int(i)
  if i < cur_i: raise Exception("got i=%d but cur_i=%d. is input 'sort -n'd ?" % (i,cur_i))
  while i > cur_i:
    print("")
    cur_i += 1
  print(j,':',val,  sep='', end=' ')
