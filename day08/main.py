import re

def paintMap(sigmap, orig, steps):
	pos1 = [steps[0]-orig[0]+steps[0], steps[1]-orig[1]+steps[1]]
	pos2 = [orig[0]-steps[0]+orig[0], orig[1]-steps[1]+orig[1]]
	# print(orig, steps)
	for i in range(len(sigmap)):
		if i == pos1[1] or i == pos2[1]:
			l = ""
			for j in range(len(sigmap[i])):
				if i == pos1[1] and j == pos1[0]:
					l+= '#'
				elif i == pos2[1] and j == pos2[0]:
					l+= '#'
				else:
					l += sigmap[i][j]
			sigmap[i] = l

def copyMap(map):
	sigmap = []
	for line in map:
		l = ""
		for c in line:
			l += "."
		sigmap.append(l)
	return sigmap

def countSignals(sigmap):
	cou = 0
	# print(sigmap)
	for line in sigmap:
		for c in line:
			if c == '#':
				cou+=1
	return cou

def testSignals(map, signals):
	sigmap = copyMap(map)
	for i in range(len(signals)):
		# print("=========")
		for j in range(len(map)):
			orig = [0,0]
			idx = map[j].find(signals[i])
			if idx >= 0:
				orig = [idx, j]
				for k in range(len(map)):
					if k == j:
						continue
					sec = [0,0]
					idy = map[k].find(signals[i])
					if idy >= 0:
						sec = [idy, k]
						paintMap(sigmap, orig, sec)
	return countSignals(sigmap)


with open("input.txt", "r") as data:
	map = []
	signals = ""
	count = 0
	for line in data:
		map.append(line.strip())
		for c in line:
			if c != '.' and c not in signals:
				signals += c
	count = testSignals(map, signals)
	print(count)