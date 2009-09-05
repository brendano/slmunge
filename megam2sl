#!/usr/bin/env python2.6
# megam format: http://www.cs.utah.edu/~hal/megam/

from __future__ import print_function
import json, shelve, sys
from collections import defaultdict
def uniq_c(seq):
  ret = defaultdict(lambda:0)
  for x in seq:
    ret[x] += 1
  return dict(ret)

def myjoin(seq, sep=u" "):
  " because str.join() is annoying "
  return sep.join(unicode(x) for x in seq)


#minfc = 10
#EMPTY = {'counts':(0,0)}
#model = util.DefaultMapping(shelve.open("nb.s"), lambda:EMPTY)
# model = defaultdict(lambda:EMPTY)
# model.update(json.load(open("nb.json")))

FEAT_C=0
def inc_c():
  global FEAT_C
  FEAT_C+=1
  return FEAT_C
feat2id = defaultdict(inc_c)

for line in sys.stdin:
  s=line.strip()
  if s=="DEV" or s=="TEST":
    print(s)
    continue
  
  label,feats = line.split("\t")
  # feats = [f for f in feats.split()  if sum(model[f]['counts']) >= minfc]

  # the bernoulli implicit format
  feats = [f for f in feats.split()]
  feats = [(f_str, feat2id[f_str], count) for f_str,count in uniq_c(feats).iteritems()]
  feats.sort(key= lambda (_s,f_id,_c): f_id)
  
  label = {'0':'-1', '1':'1'}[label]
  # print(feat2id['asdf'])
  #print("%s\t%s" % (label, 
  #        myjoin(["%d:%d" % (f_id, count)  for (f_str, f_id, count) in feats], sep=" ")) )
  print(label, end='\t')
  print(*("%d:%d" % (f_id, count) for (f_str,f_id,count) in feats), sep=' ')

#import shelve
#feat2id_s = shelve.open("feat2id.s","n")
#id2feat_s = shelve.open("id2feat.s","n")
#for f,i in util.counter(  feat2id.iteritems()  ):
#  feat2id_s[f] = i
#  id2feat_s[str(i)] = f
#feat2id_s.close()
#id2feat_s.close()
