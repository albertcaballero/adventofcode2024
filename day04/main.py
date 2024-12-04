def searchDiag(lines, i, j):
	sm = 0
	# print (len(lines[i]))
	# print (i, j)
	if i < len(lines) - 3:
		if j<len(lines[i]) -3 and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
			sm +=1
		if j>=3 and lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
			sm +=1
	if  i >= 3:
		if j<len(lines[i]) - 3 and lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
			sm +=1
		if j>=3 and lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
			sm +=1
	return sm
	


def searchVert(lines, i, j):
	sm = 0
	if i <= len(lines) - 3:
		if lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
			sm +=1
	if  i >= 3:
		if lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S':
			sm +=1
	return sm
	


def lookX(lines, i, j):
	xm = 0
	if j>=3 and lines[i][j-1] == 'M' and lines[i][j-2] == 'A' and lines[i][j-3] == 'S':
		xm += 1
	if j<len(lines[i]) - 3 and lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S':
		xm += 1
	xm += searchVert(lines, i, j)
	xm += searchDiag(lines, i, j)
	return xm

with open("input.txt", "r") as data:
	lines = []
	xmas = 0
	for line in data:
		lines.append(line)
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] == 'X':
				xmas += lookX(lines, i, j);
	print (xmas)