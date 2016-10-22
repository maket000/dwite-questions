datafile = open("DATA4")
r, c = map(int, datafile.readline().rstrip('\n').split('\n'))
grid = [datafile.readline.rstrip('\n').upper() for _ in xrange(r)]
words = [datafile.readline.rstrip('\n').upper() for _ in xrange(5)]
datafile.close()

outfile = open("DATA4", 'w')

for word in words:
	lookqueue = []
	for y in xrange(r):
		for x in xrange(c):
			if word[0] == grid[y][x]:
				lookqueue.append(((y,x), 1, [(y,x)]))
	while lookqueue:
		cur = lookqueue.pop()
		if cur[1] == len(word):
			path = cur[2]
			break
		for ny in xrange(cur[0][0]-1, cur[0][0]+2):
			for nx in xrange(cur[0][1]-1, cur[0][1]+2):
				if 0 <= cur[0][0] < r and 0 <= cur[0][1] < c:
					if grid[ny][nx] == word[n] and (ny,nx) not in cur[2]:
						lookqueue.append((e(ny,nx), n+1, cur[2] + [(ny,nx)]))

	toprow = r
	leftcol = c
	for p in path:
		if p[0] < toprow:
			toprow = p[0]
		if p[1] < leftcol:
			leftcol = p[1]

	outfile.write("%d %d\n" % (toprow, leftcol))

outfile.close()