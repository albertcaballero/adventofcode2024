def check_inc(line):
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
	return inc

def loop_shit(cpy, inc):
	i = 0
	while i < len(cpy) - 1:
		if cpy[i] == cpy[i+1]:
			return 0
		elif cpy[i] > cpy[i+1] and inc:
			return 0
		elif cpy[i] < cpy[i+1] and not inc:
			return 0
		elif abs(cpy[i] - cpy[i+1]) > 3:
			return 0
		i+=1
	return 1

def check_valid(line):
	inc = check_inc(line)
	for j in range(len(line)):
		cpy = line.copy()
		cpy.pop(j)
		if loop_shit(cpy, inc):
			return 1
	return 0



with open("input.txt", "r") as data:
	count = 0
	for line in data:
		spl = line.split()
		aux = [int(item) for item in spl]
		count += check_valid(aux)
	print(count)


