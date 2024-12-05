
def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

def  checkUpdate(rules, updates):
	mid = 0
	for update in updates:
		invalid = False
		for j in range(len(update)):
			for rule in rules:
				if update[j]==rule[1]:
					for num2 in update[j:]:
						if num2 == rule[0]:
							invalid = True
		if not invalid:
			mid += findMiddle(update)
	return mid




with open("input.txt", "r") as data:
	rules = []
	updates=[]
	u=[]
	r = []
	for line in data:
		if line.find("|") > 0:
			r = line.split("|")
			aux = [int(item) for item in r]
			rules.append(aux)
			if line.strip() == "":
				break
		elif line.find(",") > 0:
			u = line.split(",")
			aux = [int(item) for item in u]
			updates.append(aux)
	print(checkUpdate(rules, updates))
	