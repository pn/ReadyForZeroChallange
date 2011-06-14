#!/usr/bin/env python
import sys
s = open('1').read().strip()
hashes = {}
for i in xrange(len(s)-4):
	seq = s[i:i+5]
	hashes[seq] = []
	for j in xrange(5):
		ss = 0
		for k in xrange(5):
			if k != j:
				ss+=ord(seq[k])
				ss*=256
		ss/=256
		hashes[seq].append(str(ss))
k = hashes.keys()
for i in xrange(5):
	for g in xrange(len(k)):
		for h in xrange(g, len(k)):
			if g == h:
				continue
			if hashes[k[g]][i] == hashes[k[h]][i]:
				print k[g][:i]+k[g][i+1:]
				sys.exit(0)
