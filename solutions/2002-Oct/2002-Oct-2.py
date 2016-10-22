datafile = open("DATA2")
outfile = open("OUT2", 'w')

for _ in xrange(5):
	monthly = float(datafile.readline().rstrip('\n'))
	rate = 1 + (float(datafile.readline().rstrip('\n')) / (100*12))
	length = int(datafile.readline().rstrip('\n')) * 12

	total = 0
	for _ in xrange(length):
		total = round((total+monthly)*rate, 2)

	outfile.write("%.2f\n" % (total))

datafile.close()
outfile.close()
