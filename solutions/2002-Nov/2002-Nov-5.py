# This question is absurdly easy for question 5

A = ord('A')
Z = ord('Z')

letters = [chr(c) for c in xrange(A, Z+1)]

datafile = open("DATA5")
outfile = open("OUT5", 'w')

for _ in xrange(5):
	counts = [0 for _ in xrange(Z+1)]
	for c in datafile.readline().rstrip('\n'):
		if c.isalpha():
			counts[ord(c.upper())] += 1
	outstrs = []
	for letter in xrange(A, Z+1):
		if counts[letter]:
			outstrs.append("%s-%d" % (chr(letter), counts[letter]))
	outfile.write("%s\n" % (':'.join(outstrs)))

datafile.close()
outfile.close()
