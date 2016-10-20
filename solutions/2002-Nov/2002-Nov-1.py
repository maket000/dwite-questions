datafile = open("DATA1")
outfile = open("OUT1", 'w')

for _ in xrange(5):
	top = 0
	for _ in xrange(3):
		reg = float(datafile.readline().rstrip('\n'))
		sale = float(datafile.readline().rstrip('\n'))
		off = 100 - sale/reg
		if off > top:
			top = off
	outfile.write("%s\n" % (("%.3f" % (top)).rjust(7)))

datafile.close()
outfile.close()
