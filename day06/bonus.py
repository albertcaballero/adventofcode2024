def nextPos(guard, map):
	if guard[2] == 0:
		if guard[1] - 1 < 0:
			return [-1,-1,-1]
		if map[guard[1]-1][guard[0]] =='#' or map[guard[1]-1][guard[0]] =='O':
			return [guard[0], guard[1], 1]
		return [guard[0], guard[1]-1, 0]
	if guard[2] == 1:
		if guard[0] + 1 >= len(map[0]):
			return [-1,-1,-1]
		if map[guard[1]][guard[0]+1] =='#' or map[guard[1]][guard[0]+1] =='O':
			return [guard[0], guard[1], 2]
		return [guard[0]+1, guard[1], 1]
	if guard[2] == 2:
		if guard[1] + 1 >= len(map):
			return [-1,-1,-1]
		if map[guard[1]+1][guard[0]] =='#' or map[guard[1]+1][guard[0]] =='O':
			return [guard[0], guard[1], 3]
		return [guard[0], guard[1]+1, 2]
	if guard[2] == 3:
		if guard[0] - 1 < 0:
			return [-1,-1,-1]
		if map[guard[1]][guard[0]-1] =='#' or  map[guard[1]][guard[0]-1] =='O':
			return [guard[0], guard[1], 0]
		return [guard[0]-1, guard[1], 3]

def shouldExit(guard, map):
	if guard[0] < len(map[0]) and guard[0] >= 0 and guard[1] >= 0 and guard[1] < len(map):
		return False
	return True

def changeChar(line, ch, pos):
	if line[pos] == '#' or line[pos] == '^':
		return line
	walked = ""
	for i in range(len(line)):
		if i == pos:
			walked += ch
		else:
			walked += line[i]
	return walked

def checkLoop(positions, guard):
	if guard == [-1,-1,-1]:
		return False
	for pos in positions:
		if guard[0] == pos[0] and guard[1] == pos[1] and guard[2] == pos[2]:
			return True
	return False

def mapPath(guard, map):
	count = 0
	for j in range(len(map)):
		for i in range(len(map[j])):
			print (j, i)
			map[j] = changeChar(map[j], 'O', i)
			positions = []
			guard = [85, 65, 0]
			while not shouldExit(guard, map):
				positions.append(guard.copy())
				guard = nextPos(guard, map)
				if checkLoop(positions, guard):
					count+=1
					break
			map[j] = changeChar(map[j], '.', i)
	return count


with open("input.txt", "r") as data:
	map = []
	count = 0
	lc = 0
	guard = [0,0, 0]
	for line in data:
		map.append(line.strip())
		pos = line.find("^")
		if pos > 0:
			guard = [pos, lc, 0]
		lc += 1
	print(guard)
	count = mapPath(guard, map)
	print (count)