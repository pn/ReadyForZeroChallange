#!/usr/bin/env python
s = open('2').read().strip()
result = 0
for i in xrange(0, len(s), 2):
	try:
		result += int(s[i])
	except ValueError:
		pass
print result
