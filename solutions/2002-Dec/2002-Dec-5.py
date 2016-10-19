datafile = open("DATA5")
outfile = open("OUT5", 'w')

for _ in xrange(5):
	piles = map(int, datafile.readline().rstrip('\n').split()[2:])
	piles.sort()
	past = []
	past.append(piles[:])
	count = 1
	while True: # Safe!
	    piles = filter(lambda p: p!=0, map(lambda p: p-1, piles) + [len(piles)])
	    piles.sort()
	    if piles == past[-1]:
	    	result = "WIN"
	    	count -= 1
	    	break
	    if piles in past:
	    	result = "LOSS"
	    	break
	    past.append(piles[:])
	    count += 1

	outfile.write("%s-%d\n" % (result, count))

datafile.close()
outfile.close()
