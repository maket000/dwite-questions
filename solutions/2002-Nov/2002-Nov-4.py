datafile = open("DATA4")
board = [[int(space) for space in rank.split()]
         for rank in datafile.read().rstrip('\n').split('\n')]
datafile.close()

rows, cols = len(board), len(board[0])

topsums = [0 for _ in xrange(cols)]
topsums[-1] = board[0][-1]
for c in xrange(cols-2, -1, -1):
	topsums[c] = topsums[c+1] + board[0][c]

sidesums = [board[0][-1]]
for r in xrange(1, rows):
	sidesums.append(sidesums[r-1] + board[r][-1])


top5 = []

# (row, column, total)
posqueue = [(rows-1, 0, 0)]
while posqueue:
	cur = posqueue.pop()
	if cur[0] == 0:
		top5.append(cur[2] + topsums[cur[1]])
		top5.sort()
		top5 = top5[-5:]
	elif cur[1] == cols-1:
		top5.append(cur[2] + sidesums[cur[0]])
		top5.sort()
		top5 = top5[-5:]
	else:
		posqueue.append((cur[0]-1, cur[1], cur[2]+board[cur[0]][cur[1]]))
		posqueue.append((cur[0], cur[1]+1, cur[2]+board[cur[0]][cur[1]]))

outfile = open("OUT4", 'w')
outfile.write('\n'.join(top5) + '\n')
outfile.close()
