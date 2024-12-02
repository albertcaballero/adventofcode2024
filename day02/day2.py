def check_valid(line):
	inc = True
	if line[0] > line[1]:
		inc = False
	for i in range(len(line) - 1):
		if line[i] == line[i+1]:
			return 0
		if line[i] > line[i+1] and inc:
			return 0
		if line[i] < line[i+1] and not inc:
			return 0
		if abs(line[i] - line[i+1]) > 3:
			return 0
	return 1



with open("input.txt", "r") as data:
	count = 0
	for line in data:
		spl = line.split()
		aux = [int(item) for item in spl]
		count += check_valid(aux)
	print(count)


