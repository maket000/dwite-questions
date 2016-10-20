datafile = open("DATA3")
grid = [[c == 'X' for c in line]
        for line in datafile.read().rstrip('\n').split('\n')[1:]]
datafile.close()

r, c = len(grid), len(grid[0])

for y in xrange(r):
	grid[y] = [False] + grid[y] + [False]

empty_row = [[False for _ in xrange(c+2)]]
grid = empty_row + grid + empty_row

outfile = open("OUT3", 'w')

stops = [1, 5, 10, 50, 100]
difs = [stops[0]] + [stops[i] - stops[i-1] for i in xrange(1, len(stops))]
for iters in difs:
	for _ in xrange(iters):
		neighbors = [[0 for _ in xrange(c+2)] for _ in xrange(r+2)]
		for y in xrange(1, r+1):
			for x in xrange(1, c+1):
				by = y-1
				bx = x-1
				neighbors[y][x] = sum([grid[by + i/3][bx + i%3] for i in xrange(9)]) - grid[y][x]

		for y in xrange(1, r+1):
			for x in xrange(1, c+1):
				if grid[y][x]:
					if neighbors[y][x] <= 1 or neighbors[y][x] >= 4:
						grid[y][x] = False
				else:
					if neighbors[y][x] == 3:
						grid[y][x] = True

	count = sum([sum(grid[row]) for row in xrange(1, r+1)])
	outfile.write("%d\n" % (count))
outfile.close()

