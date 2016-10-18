# Not tested whatsoever

datafile = open("DATA5")
outfile = open("OUT5", 'w')

difs = [(1,0), (-1,0), (0,1), (0,-1)]
ex_dif = [
	[0,2,3],
	[1,2,3],
	[0,1,2],
	[0,1,3]
]


for _ in xrange(5):
	rows, cols = map(int, datafile.readline().rsplit('\n').split())
	grid = [datafile.readline().rsplit('\n') for _ in xrange(rows)]

	rm1 = rows - 1
	cm1 = cols - 1

	for r in xrange(rows):
		for c in xrange(cols):
			if grid[r][c] == 'A':
				start = (r,c)
			elif grid[r][c] == 'B':
				end = (r,c)

	# List of ((r, c), allowed, length)
	pos_queue = [((start), range(4), 0)]
	while True:
		state = pop(0)
		if state[0] == end:
			distance = state[2] - 1
			break

		allowed = []
		for d in xrange(len(state[1])):
			nr = r + difs[state[1][d]][0]
			nc = c + difs[state[1][d]][1]
			if (0 < nr < rm1 and 0 < nc < cm1 and
				grid[nr][nc] != '#'):
			    pos_queue.append(((nr,nc),
			    	              ex_dif[state[1][d]],
			    	              state[0] + 1))
	outfile.write("%d\n" % (distance))

datafile.close()
outfile.close()