#/usr/bin/python
import commands
d = {}
f = commands.getoutput
for i in range(1000):
	r = f('./c_aslr system')
	o = str(r).split(':')
	d.setdefault(str(o[1]), 0)
	d[str(o[1])] += 1
maxval = 0
maxkey = 0
for i in d.keys():
	if maxval < d[i]:
		maxval = d[i]
		maxkey = i
print str(maxkey) + ":" + str(maxval)

