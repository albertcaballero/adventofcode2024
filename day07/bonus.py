
def testCalc(res, eq, current=0, index=0):
	if index == len(eq):
		if current == res:
			return res
		return -1
	
	if testCalc(res, eq, current + eq[index], index + 1) > 0:
		return current
	if testCalc(res, eq, current * eq[index], index + 1) > 0:
		return current
	if testCalc(res, eq, current*pow(10, len(str(eq[index])))+eq[index], index + 1) > 0:
		return current
	return -1


def calculate(res, eq):
	n = testCalc(res, eq, 0, 0)
	# print (n)
	if n == 0:
		return res
	return 0


with open("input.txt", "r") as data:
	eq = []
	res = []
	count = 0
	for line in data:
		aux = line.split(":")
		res.append(int(aux[0]))
		spl = aux[1].split()	
		aux2 = [int(item) for item in spl]
		eq.append(aux2)
	for i in range(len(res)):
		count += calculate(res[i], eq[i])
	print(count)