INTEREST = map(str, range(1,6))
PORTAL_IN = map(chr, range(ord('a'), ord('j')+1))
PORTAL_OUT = map(chr, range(ord('A'), ord('J')+1))
FLOOR = '.'
WALL ='#'

MOVEMENT = [(1,0), (-1,0), (0,1), (0,-1)]


datafile = open("DATA5.txt")
rows = int(datafile.readline().rstrip('\n'))
cols = int(datafile.readline().rstrip('\n'))
grid = [list(line) for line in datafile.read().rstrip('\n').split('\n')]
datafile.close()

portal_ins = [] # portals in room by index
portal_outs = {} # rooms that portals are in by portal letter

starting_rooms = [None for _ in xrange(5)]

for start_y in xrange(rows):
    for start_x in xrange(cols):
        if grid[start_y][start_x] != '#':
            portal_ins_room = []
            tr_queue = [(start_y, start_x)]
            while tr_queue:
                pos = tr_queue.pop()
                if grid[pos[0]][pos[1]] != '#':
                    cur = grid[pos[0]][pos[1]]
                    if cur in PORTAL_IN:
                        portal_ins_room.append(cur)
                    elif cur in PORTAL_OUT:
                        portal_outs[cur.lower()] = len(portal_ins)
                    elif cur in INTEREST:
                        starting_rooms[int(cur)-1] = len(portal_ins)
                    grid[pos[0]][pos[1]] = '#'

                    for dy, dx in MOVEMENT:
                        new_y = pos[0] + dy
                        new_x = pos[1] + dx
                        if (0 <= new_y < rows) and (0 <= new_x < cols):
                            tr_queue.append((new_y, new_x))

            portal_ins.append(portal_ins_room)

outfile = open("OUT5.txt", 'w')

for start in xrange(len(starting_rooms)):
    reached = []
    rooms_to_visit = [starting_rooms[start]]
    visited = []
    while rooms_to_visit:
        current = rooms_to_visit.pop()
        if current not in visited:
            visited.append(current)
            for i in xrange(len(starting_rooms)):
                if starting_rooms[i] == current and i != start:
                    reached.append(i)

            for portal in portal_ins[current]:
                rooms_to_visit.append(portal_outs[portal])
    if start in reached:
        reached.remove(start)
    reached.sort()
    outfile.write("%d:%s\n" % (start+1, ' '.join(map(lambda r: str(r+1), reached))))

outfile.close()