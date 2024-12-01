with open("input.txt", "r") as data:
	first = []
	second = []
	for line in data:
		aux = line.split()
		first.append(aux[0])
		second.append(aux[1])
	first.sort()
	second.sort()
	sum = 0	
	for i in range(len(first)):
		sum += abs(int(first[i])-int(second[i]))
	print(sum)