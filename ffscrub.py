#!/usr/local/bin/python



with open(file) as f:
	content = f.readlines()

	for line in content:
		statline = StatLine(line.rstrip())
		self.statlines.append(statline)

