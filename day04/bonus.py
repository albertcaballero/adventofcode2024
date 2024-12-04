def checkS(lines, i, j):
	s = 0
	if lines[i-1][j-1] == 'S':
		s += 1
	if lines[i+1][j+1] == 'S':
		s +=1
	if s == 2 or s == 0:
		return False
	if lines[i+1][j-1] == 'S' and lines[i-1][j+1] != 'S':
		return True
	if lines[i+1][j-1] != 'S' and lines[i-1][j+1] == 'S':
		return True
	
def checkM(lines, i, j):
	s = 0
	if lines[i-1][j-1] == 'M':
		s += 1
	if lines[i+1][j+1] == 'M':
		s +=1
	if s == 2 or s == 0:
		return False
	if lines[i+1][j-1] == 'M' and lines[i-1][j+1] != 'M':
		return True
	if lines[i+1][j-1] != 'M' and lines[i-1][j+1] == 'M':
		return True

def lookA(lines, i, j):
	if i < len(lines)-1 and i > 0 and j < len(lines[i]) and j>0:
		if checkS(lines, i, j) and checkM(lines, i, j):
			return 1
	return 0

with open("input.txt", "r") as data:
	lines = []
	xmas = 0
	for line in data:
		lines.append(line)
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] == 'A':
				xmas += lookA(lines, i, j);
	print (xmas)