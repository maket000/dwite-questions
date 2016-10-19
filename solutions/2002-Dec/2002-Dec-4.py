from math import sqrt

def dist(p1, p2):
	return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def heron(p1, p2, p3):
	a = dist(p1, p2)
	b = dist(p2, p3)
	c = dist(p3, p1)
	s = (a + b + c) / 2
	asq = s*(s-a)*(s-b)*(s-c)
	return sqrt(asq)

datafile = open("DATA4")
outfile = open("OUT4", 'w')

for _ in xrange(5):
	c = map(int, datafile.readline().rstrip('\n').split())
	p1 = (c[0], c[1])
	p2 = (c[2], c[3])
	p3 = (c[4], c[5])
	area = heron(p1, p2, p3)
	if area:
		outfile.write("%.2f\n" % (area))
	else:
		outfile.write("NOT POSSIBLE\n")

datafile.close()
outfile.close()
