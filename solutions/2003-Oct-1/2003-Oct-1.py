datafile = open("DATA1")
outfile = open("OUT1", 'w')

for _ in xrange(5):
	corners = map(int, datafile.readline().rstrip('\n').split())
	area = abs((corners[2]-corners[0]) * (corners[3]-corners[1]))
	outfile.write("%d\n" % (area))

datafile.close()
outfile.close()