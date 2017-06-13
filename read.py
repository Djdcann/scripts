import re

tokens = {}

file = open("keys.txt")
for line in file.readlines():
	line = line.replace("\n", "")
	m = re.search(r"(\w+)\|(.+?) (\w+)", line)
	print line
	print m.group(1), m.group(2), m.group(3)
	#insert value into tokens
	tokens[m.group(1)] = (m.group(2), m.group(3))

print tokens
file.close()