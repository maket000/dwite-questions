datafile = open("DATA1")
outfile = open("OUT1", 'w')

for _ in xrange(5):
	rate = float(datafile.readline().rstrip('\n'))
	hours = int(datafile.readline().rstrip('\n'))
	pay = hours * rate
	hours -= 15
	if hours > 0:
		pay += hours * rate
		hours -= 5
		if hours > 0:
			pay += hours * rate
	outfile.write("%.f\n" % (rount(pay, 2)))

datafile.close()
outfile.close()