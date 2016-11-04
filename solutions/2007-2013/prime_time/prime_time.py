def sieve(n):
    b = [True]*n
    b[0], b[1] = False, False
    p = []
    for i in xrange(2, n):
        if b[i]:
            p.append(i)
            for r in xrange(i*2, n, i):
                b[r] = False
    return p

primes = sieve(10001)

datafile = open("DATA2.txt")
outfile = open("OUT2.txt", 'w')

for _ in xrange(5):
    ints = range(2, int(datafile.readline().rstrip('\n')) + 1)
    facts = {}
    for i in ints:
        pi = 0
        while i > 1:
            while i % primes[pi] == 0:
                i /= primes[pi]
                if primes[pi] in facts:
                    facts[primes[pi]] += 1
                else:
                    facts[primes[pi]] = 1
            pi += 1

    outstr = []
    bases = facts.keys()
    bases.sort()
    for base in bases:
        outstr.append("%d^%d" % (base, facts[base]))
    outfile.write("%s\n" % (" * ".join(outstr)))

datafile.close()
outfile.close()