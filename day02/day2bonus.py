def check_valid(line):
	bad = 0
	inc = True
	c = 0
	for a in range(len(line) - 1):
		if line[a] > line[a+1]:
			c += 1
		elif line[a] == line[a+1]:
			c += 0
		else:
			c -= 1
	if c > 0:
		inc = False
	i = 0
	while i < len(line) - 1:
		if line[i] == line[i+1]:
			bad += 1
		elif line[i] > line[i+1] and inc:
			bad += 1
		elif line[i] < line[i+1] and not inc:
			bad += 1
		elif abs(line[i] - line[i+1]) > 3:
			bad += 1
		if bad == 1:
			line.pop(i+1)
		i+=1
	# print (bad)
	if bad > 1:
		return 0
	return 1



with open("input.txt", "r") as data:
	count = 0
	for line in data:
	# line = "61 68 69 71 72 79"
		spl = line.split()
		aux = [int(item) for item in spl]
		count += check_valid(aux)
	print(count)


