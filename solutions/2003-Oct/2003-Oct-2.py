rates = [0.275635, 0.045293, 0.08811, 0.103994]

def round_up(n, digits=2):
	return round(n + 5*(10**-(digits+1)), digits)


datafile = open("DATA2")
outfile = open("OUT2", 'w')

for _ in xrange(5):
	volume = float(datafile.readline().rstrip('\n'))
	pre_tax = sum(map(lambda r: round_up(r*volume), rates)) + 10.00
	after_tax = round(pre_tax + round_up(pre_tax*0.07), 2)
	datafile.write("%.2f\n" % (after_tax))

datafile.close()
outfile.close()
