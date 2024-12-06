def nextPos(guard, map):
	if guard[2] == 0:
		if guard[1] - 1 < 0:
			return [-1,-1,-1]
		if map[guard[1]-1][guard[0]] =='#':
			return [guard[0], guard[1], 1]
		return [guard[0], guard[1]-1, 0]
	if guard[2] == 1:
		if guard[0] + 1 >= len(map[0]):
			return [-1,-1,-1]
		if map[guard[1]][guard[0]+1] =='#':
			return [guard[0], guard[1], 2]
		return [guard[0]+1, guard[1], 1]
	if guard[2] == 2:
		if guard[1] + 1 >= len(map):
			return [-1,-1,-1]
		if map[guard[1]+1][guard[0]] =='#':
			return [guard[0], guard[1], 3]
		return [guard[0], guard[1]+1, 2]
	if guard[2] == 3:
		if guard[0] - 1 < 0:
			return [-1,-1,-1]
		if map[guard[1]][guard[0]-1] =='#':
			return [guard[0], guard[1], 0]
		return [guard[0]-1, guard[1], 3]

def shouldExit(guard, map):
	if guard[0] < len(map[0]) and guard[0] >= 0 and guard[1] >= 0 and guard[1] < len(map):
		return False
	return True

def mapPath(guard, map):
	count = 0
	while not shouldExit(guard, map):
		guard = nextPos(guard, map)
		if map[guard[1]][guard[0]] == '.':
			count+=1
		walked =""
		for i in range(len(map[guard[1]])):
			if i == guard[0]:
				walked += 'X'
			else:
				walked += map[guard[1]][i]
		map[guard[1]] = walked
	return count


with open("input.txt", "r") as data:
	map = []
	count = 0
	lc = 0
	guard = [0,0, 0]
	for line in data:
		map.append(line)
		pos = line.find("^")
		if pos > 0:
			guard = [pos, lc, 0]
		lc += 1
	print (guard)
	count = mapPath(guard, map)
	print (count)