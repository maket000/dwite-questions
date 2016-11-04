def sieve(n):
    b = [True]*n
    b[0], b[1] = False, False
    p = []
    for i in xrange(2, n):
        if b[i]:
            p.append(i)
            for r in xrange(i*2, n, i):
                b[r] = False
    return b

primes = sieve(1000)

datafile = open("DATA1.txt")
outfile = open("OUT1.txt", 'w')

outfile.write('\n'.join(["prime" if primes[int(line.rstrip('\n'))] else "not" for line in datafile.read().rstrip('\n').split('\n')]))

datafile.close()
outfile.close()