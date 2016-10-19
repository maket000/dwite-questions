datafile = open("DATA3")
outfile = open("OUT3", 'w')

MAX_SIZE = 8000000

for _ in xrange(5):
	vols = map(int, datafile.readline().rstrip('\n').split()[1:])
	n = len(vols)
	bitmasks = [1 << i for i in xrange(n)]
	top = 0
	for combo in xrange(1, 2**n):
		size = 0
		for p in xrange(n):
			if combo & bitmasks[p]:
				size += vols[p]
		if top < size <= MAX_SIZE:
			top = size
	outfile.write("%d\n" % (top))


datafile.close()
outfile.close()
