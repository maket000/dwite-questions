datafile = open("DATA2.txt")
outfile = open("OUT2.txt", 'w')

for _ in xrange(5):
    n, code = datafile.readline().rstrip('\n').split()
    n = int(n)
    while n > 9:
        n = sum(map(int, str(n)))
    if (n-1) + ord('A') == ord(code):
        outfile.write("match\n")
    else:
        outfile.write("error\n")

datafile.close()
outfile.close()