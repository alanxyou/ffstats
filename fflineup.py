#!/usr/local/bin/python

from ffstatline import *


class Lineup:
	def __init__(self, slots):
		self.qb = slots[0]
		self.rb = slots[1]
		self.wr = slots[2]
		self.te = slots[3]
		self.flex = slots[4]
		self.dst = slots[5]
		self.k = slots[6]

		self.total_score = self.calc_total_score()


	def qb_score(self):
		return self.qb[0].points


	def qb_percentage(self):
		return float(self.qb[0].points) / self.total_score * 100


	def rb_score(self):
		return self.rb[0].points + self.rb[1].points


	def rb_avg_score(self):
		return (self.rb[0].points + self.rb[1].points) / 2.0


	def rb_percentage(self):
		return float(self.rb[0].points + self.rb[1].points) / self.total_score * 100


	def wr_score(self):
		return self.wr[0].points + self.wr[1].points


	def wr_avg_score(self):
		return (self.wr[0].points + self.wr[1].points) / 2.0


	def wr_percentage(self):
		return float(self.wr[0].points + self.wr[1].points) / self.total_score * 100


	def te_score(self):
		return self.te[0].points


	def te_percentage(self):
		return float(self.te[0].points) / self.total_score * 100


	def flex_score(self):
		return self.flex[0].points


	def flex_percentage(self):
		return float(self.flex[0].points) / self.total_score * 100


	def dst_score(self):
		return self.dst[0].points


	def dst_percentage(self):
		return float(self.dst[0].points) / self.total_score * 100


	def k_score(self):
		return self.k[0].points


	def k_percentage(self):
		return float(self.k[0].points) / self.total_score * 100


	def calc_total_score(self):
		score = 0

		score += self.qb[0].points
		score += self.rb[0].points
		score += self.rb[1].points
		score += self.wr[0].points
		score += self.wr[1].points
		score += self.te[0].points
		score += self.flex[0].points
		score += self.dst[0].points
		score += self.k[0].points

		return score


	def print_lineup(self):
		print self.qb[0]
		print self.rb[0]
		print self.rb[1]
		print self.wr[0]
		print self.wr[1]
		print self.te[0]
		print self.flex[0]
		print self.dst[0]
		print self.k[0]

