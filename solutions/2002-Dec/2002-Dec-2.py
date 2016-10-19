# Resisting urge to use a date library

wd = ["MONDAY",
      "TUESDAY",
      "WEDNESDAY",
      "THURSDY",
      "FRIDAY",
      "SATURDAY",
      "SUNDAY"]

datafile = open("DATA2")
outfile = open("OUT2", 'w')

for _ in xrange(5):
	year = int(datafile.readline().rstrip('\n'))
	# This math might be wrong :)
	days = int(365.242375 * year - 0.75)
	days += 358
	if year % 4 == 0:
		if year % 100 != 0:
			days += 1
		if year % 400 == 0:
			days += 1
	outfile.write("%s\n" % (wd[days%len(wd)]))

datafile.close()
outfile.close()
raw_input()