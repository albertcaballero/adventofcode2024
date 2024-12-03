import re

with open("input.txt", "r") as data:
	result = 0
	str = data.read()
	donts = re.split("don't\(\)", str)
	x = re.findall("mul\([0-9]{0,3},[0-9]{0,3}\)", donts[0])
	for mul in donts[1:]:
		do = mul.find("do()")
		if do < 0:
			continue
		dos = mul[do:]
		x += re.findall("mul\([0-9]{0,3},[0-9]{0,3}\)", dos)


	for el in x:
		fs = int(el[4:el.find(",")])
		s = int(el[el.find(",")+1:-1])
		result += fs*s
	print (result)