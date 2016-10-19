firstwins = [7, 11]
firstloss = [2, 3, 10]
midloss = [7, 10, 11]

datafile = open("DATA1")
outfile = open("OUT1", 'w')

for _ in xrange(5):
	rolls = map(int, datafile.readline().rstrip('\n').split())
	if rolls[0] in firstwins:
		result = "WIN"
		rollnum = 1
	elif rolls[0] in firstloss:
		result = "LOSS"
		rollnum = 1
	else:
		result = "NO RESULT"
		rollnum = len(rolls) - 1
		for r in xrange(1, len(rolls)):
			if rolls[r] in midloss:
				result = "LOSS"
				rollnum = r + 1
				break
			elif rolls[r] = rolls[0]:
				result = "WIN"
				rollnum = r + 1
				break
	outfile.write("%s-%d\n" % (result, rollnum))

datafile.close()
outfile.close()
