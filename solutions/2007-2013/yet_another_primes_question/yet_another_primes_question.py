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

primes = sieve(1000)

def valid(n):
    factors = []
    for p in primes:
        while n % p == 0:
            if (factors and p == factors[-1]) or len(factors) >= 3:
                return "not"
            factors.append(p)
            n /= p
    return "valid" if len(factors) == 3 else "not"


datafile = open("DATA1.txt")
outfile = open("OUT1.txt", 'w')

outfile.write('\n'.join(map(valid, map(int, datafile.read().rstrip('\n').split('\n')))))

datafile.close()
outfile.close()