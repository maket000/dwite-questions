#lazy solution

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

primes = sieve(100001)
primes.append(100001)

datafile = open("DATA2.txt")
outfile = open("OUT2.txt", 'w')

for _ in xrange(5):
    cap = int(datafile.readline().rstrip('\n'))
    i = 0
    total = 0
    while primes[i] <= cap:
        total += primes[i]
        i += 1
    outfile.write("%d\n" % (total))

datafile.close()
outfile.close()