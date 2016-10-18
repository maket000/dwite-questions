lines = ["qwertyuiop",
	     "asdfghjkl",
	     "zxcvbnm"]
up_lines = map(lambda line: line.upper(), lines)

line_maps = [{lines[line][i]: lines[line][i-2]
              for i in range(len(lines[line]))}
             for line in range(len(lines))]
maps = line_maps[0].copy()
maps.update(line_maps[1])
maps.update(line_maps[2])
line_up_maps = [{up_lines[line][i]: up_lines[line][i-2]
                 for i in range(len(up_lines[line]))}
                for line in range(len(up_lines))]
up_maps = line_up_maps[0].copy()
up_maps.update(line_up_maps[1])
up_maps.update(line_up_maps[2])

def decode(letter):
	if letter.islower():
		return maps[letter]
	elif letter.isupper():
		return up_maps[letter]
	else:
		return letter

datafile = open("DATA3")
outfile = open("OUT3", 'w')
outfile.write(map(decode, datafile.read()))
outfile.close()
datafile.close()