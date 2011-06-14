#!/usr/bin/env python
import sys
s = [int(x) for x in open('3').read().strip()]
for i in xrange(1, len(s)):
	s1 = sum(s[0:i])
	j = i
	num = 1
	while j < len(s):
		k = j+1
		while k <= len(s) and sum(s[j:k]) < s1:
			k+=1
		if sum(s[j:k]) == s1:
			num+=1
			j=k
		else:
			break
		if k == len(s):
			print num
			sys.exit(0)
