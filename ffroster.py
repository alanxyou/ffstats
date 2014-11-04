#!/usr/local/bin/python

from ffstatline import *
from fflineup import *


class Roster:
	def __init__(self, roster_file):
		self.statlines = []
		self.import_roster(roster_file)

		self.active_lineup = Lineup(self.get_active_lineup())
		self.optimal_lineup = Lineup(self.get_optimal_lineup())


	def __str__(self):
		return '\n'.join([statline.__str__() for statline in self.statlines])


	def import_roster(self, roster_file):
		with open(roster_file) as f:
			content = f.readlines()

			for line in content:
				statline = StatLine(line.rstrip())
				self.statlines.append(statline)


	def get_active_lineup(self):
		[qb, rb, wr, te, dst, k, flex] = [[] for x in range(7)]

		for line in self.statlines:
			if line.slot == 'QB':
				qb.append(line)
			elif line.slot == 'RB':
				rb.append(line)
			elif line.slot == 'WR':
				wr.append(line)
			elif line.slot == 'TE':
				te.append(line)
			elif line.slot == 'FLEX':
				flex.append(line)
			elif line.slot == 'D/ST':
				dst.append(line)
			elif line.slot == 'K':
				k.append(line)

		return [qb, rb, wr, te, flex, dst, k]


	def get_optimal_lineup(self):
		[qb, rb, wr, te, dst, k, flex] = [[] for x in range(7)]

		# Separate each player by position
		for line in self.statlines:
			if line.position == 'QB':
				qb.append(line)
			elif line.position == 'RB':
				rb.append(line)
				flex.append(line)
			elif line.position == 'WR':
				wr.append(line)
				flex.append(line)
			elif line.position == 'TE':
				te.append(line)
				flex.append(line)
			elif line.position == 'D/ST':
				dst.append(line)
			elif line.position == 'K':
				k.append(line)

		# Sort players at each position by score
		qb = sorted(qb, key=lambda player: player.points, reverse=True)
		rb = sorted(rb, key=lambda player: player.points, reverse=True)
		wr = sorted(wr, key=lambda player: player.points, reverse=True)
		te = sorted(te, key=lambda player: player.points, reverse=True)
		dst = sorted(dst, key=lambda player: player.points, reverse=True)
		k = sorted(k, key=lambda player: player.points, reverse=True)
		flex = sorted(flex, key=lambda player: player.points, reverse=True)

		# Remove best position players from flex options
		for player in rb[:2]:
			flex.remove(player)
		for player in wr[:2]:
			flex.remove(player)
		for player in te[:1]:
			flex.remove(player)

		return [qb[:1], rb[:2], wr[:2], te[:1], flex[:1], dst[:1], k[:1]]


	def active_score(self):
		return self.active_lineup.total_score


	def optimal_score(self):
		return self.optimal_lineup.total_score
		
	
	def efficiency(self):
		return float(self.active_score()) / self.optimal_score()
