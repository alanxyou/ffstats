#!/usr/local/bin/python

class StatLine:
	def __init__(self, line):
		input = line.split('\t')
		self.name = input[0]
		self.position = input[1]
		self.slot = input[2]
		self.active = True if input[2] != 'BE' else  False
		self.points = int(input[3])


	def __str__(self):
		return '%s\t%s\t%s\t%s' % (self.position, self.name, self.active, self.points)

