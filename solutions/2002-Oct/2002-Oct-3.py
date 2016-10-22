
# Thanks python

datafile = open("DATA3")
outfile = open("OUT3", 'w')

outfile.write('\n'.join([round(eval(line),2) for line in datafile.read().rstrip('\n').split('\n')]))

datafile.close()
outfile.close()