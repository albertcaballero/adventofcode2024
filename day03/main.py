import re

with open("input.txt", "r") as data:
	result = 0
	str = data.read()
	x = re.findall("mul\([0-9]{0,3},[0-9]{0,3}\)", str)
	print (x)


	for el in x:
		f = int(el[4:el.find(",")])
		s = int(el[el.find(",")+1:-1])
		result += f*s
	print (result)