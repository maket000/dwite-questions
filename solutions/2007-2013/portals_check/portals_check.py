datafile = open("DATA5.txt")
outfile = open("OUT5.txt", 'w')

for _ in xrange(5):
    portals = {}
    for _ in xrange(int(datafile.readline().rstrip('\n'))):
        c, a, b = datafile.readline().rstrip('\n').split()
        if c == 'p':
            if a not in portals:
                portals[a] = set([b])
            else:
                portals[a].add(b)
            if b not in portals:
                portals[b] = set([a])
            else:
                portals[b].add(a)
        else:
            queue = [a]
            visited = []
            found = False
            while queue:
                cur = queue.pop()
                visited.append(cur)
                if cur in portals:
                    for jump in portals[cur]:
                        if jump == b:
                            outfile.write("connected\n")
                            found = True
                            break
                        if jump not in visited:
                            queue.append(jump)
                if found:
                    break
            else:
                outfile.write("not connected\n")
datafile.close()
outfile.close()