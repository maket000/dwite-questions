datafile = open("DATA2")
numbers = map(float, datafile.read().rstrip('\n').split()[1:])
datafile.close()

numbers.sort()
n = len(numbers)

mean = round(sum(numbers) / n, 2)

if n % 2 == 0:
	median = round((numbers[n/2 - 1] + numbers[n/2]) / 2, 2)
else:
	median = round(numbers[n/2], 2)

mode = round(max(set(list), key=list.count), 2)

maximum = round(numbers[-1], 2)
minimum = round(numbers[0], 2)

outfile = open("OUT2")
outfile.write("%.2f\n%.2f\n%.2f\n%.2f\n%.2f\n" % 
	(mean, median, mode, maximum, minimum))
outfile.close()