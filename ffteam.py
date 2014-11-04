#!/usr/local/bin/python

from ffroster import *
import numpy

class Team:
	def __init__(self, short_name, team_name, owner_name, week_count, file_stem):
		self.team_name = team_name
		self.owner_name = owner_name
		self.short_name = short_name
		self.weekly_rosters = []
		self.opponents = []

		self.import_rosters(week_count, file_stem)
		self.import_opponents(file_stem)


	def import_rosters(self, week_count, file_stem):
		for week_number in range(1, week_count + 1):
			self.weekly_rosters.append(Roster('{}/teams/{}/{}_{}.txt'.format(file_stem, self.short_name, self.short_name, week_number)))


	def import_opponents(self, file_stem):
		filename = '{}/teams/{}/{}_{}.txt'.format(file_stem, self.short_name, self.short_name, 'opponents')
		with open(filename) as f:
			content = f.readlines()
			self.opponents = [opponent.rstrip() for opponent in content]


	def weekly_score(self, week):
		return self.weekly_rosters[week - 1].active_score()


	def weekly_optimal_score(self, week):
		return self.weekly_rosters[week - 1].optimal_score()


	def weekly_diff(self, week):
		return self.weekly_score(week) - self.weekly_rosters[week - 1].optimal_score()


	def weekly_efficiency(self, week):
		return self.weekly_rosters[week - 1].efficiency() * 100


	def weekly_opp_score(self, league, week):
		return league.teams[self.opponents[week - 1]].weekly_score(week)


	def weekly_margin(self, league, week):
		return self.weekly_score(week) - league.teams[self.opponents[week - 1]].weekly_score(week)


	def weekly_opp_efficiency(self, league, week):
		return league.teams[self.opponents[week - 1]].weekly_efficiency(week)


	def avg_score(self):
		total_score = 0.0;

		for roster in self.weekly_rosters:
			total_score += roster.active_score()

		return (total_score / len(self.weekly_rosters))


	def avg_optimal_score(self):
		total_score = 0.0;

		for roster in self.weekly_rosters:
			total_score += roster.optimal_score()

		return (total_score / len(self.weekly_rosters))


	def avg_diff(self):
		total_diff = 0.0

		for roster in self.weekly_rosters:
			total_diff += (roster.active_score() - roster.optimal_score())

		return (total_diff / len(self.weekly_rosters))


	def avg_efficiency(self):
		total_efficiency = 0.0

		for roster in self.weekly_rosters:
			total_efficiency += (float(roster.active_score()) / roster.optimal_score())

		return (total_efficiency / len(self.weekly_rosters)) * 100


	def avg_opp_score(self, league):
		points = 0.0

		for number in range(1, len(self.weekly_rosters) + 1):
			points += league.teams[self.opponents[number - 1]].weekly_score(number)

		return points / len(self.weekly_rosters)


	def avg_margin(self, league):
		margin = 0.0

		for number, roster in zip(range(1, len(self.weekly_rosters) + 1), self.weekly_rosters):
			margin += (roster.active_score() - league.teams[self.opponents[number - 1]].weekly_score(number))

		return margin / len(self.weekly_rosters)


	def record(self, league):
		wins = 0
		losses = 0
		ties = 0

		for number, roster in zip(range(1, len(self.weekly_rosters) + 1), self.weekly_rosters):
			if roster.active_score() > league.teams[self.opponents[number - 1]].weekly_score(number):
				wins += 1
			elif roster.active_score() < league.teams[self.opponents[number - 1]].weekly_score(number):
				losses += 1
			else:
				ties += 1

		return '{}-{}-{}'.format(wins, losses, ties)


	def optimal_record(self, league):
		wins = 0
		losses = 0
		ties = 0

		for number, roster in zip(range(1, len(self.weekly_rosters) + 1), self.weekly_rosters):
			if roster.optimal_score() > league.teams[self.opponents[number - 1]].weekly_score(number):
				wins += 1
			elif roster.optimal_score() < league.teams[self.opponents[number - 1]].weekly_score(number):
				losses += 1
			else:
				ties += 1

		return '{}-{}-{}'.format(wins, losses, ties)


	def avg_opp_efficiency(self, league):
		efficiency = 0.0

		for number in range(1, len(self.weekly_rosters) + 1):
			efficiency += league.teams[self.opponents[number - 1]].weekly_efficiency(number)

		return efficiency / len(self.weekly_rosters)


	def avg_qb_score(self):
		return numpy.mean([roster.active_lineup.qb_score() for roster in self.weekly_rosters])


	def avg_qb_percentage(self):
		return numpy.mean([roster.active_lineup.qb_percentage() for roster in self.weekly_rosters])


	def avg_rb_score(self):
		return numpy.mean([roster.active_lineup.rb_score() for roster in self.weekly_rosters])


	def avg_rb_percentage(self):
		return numpy.mean([roster.active_lineup.rb_percentage() for roster in self.weekly_rosters])


	def avg_wr_score(self):
		return numpy.mean([roster.active_lineup.wr_score() for roster in self.weekly_rosters])


	def avg_wr_percentage(self):
		return numpy.mean([roster.active_lineup.wr_percentage() for roster in self.weekly_rosters])


	def avg_te_score(self):
		return numpy.mean([roster.active_lineup.te_score() for roster in self.weekly_rosters])


	def avg_te_percentage(self):
		return numpy.mean([roster.active_lineup.te_percentage() for roster in self.weekly_rosters])


	def avg_flex_score(self):
		return numpy.mean([roster.active_lineup.flex_score() for roster in self.weekly_rosters])


	def avg_flex_percentage(self):
		return numpy.mean([roster.active_lineup.flex_percentage() for roster in self.weekly_rosters])


	def avg_dst_score(self):
		return numpy.mean([roster.active_lineup.dst_score() for roster in self.weekly_rosters])


	def avg_dst_percentage(self):
		return numpy.mean([roster.active_lineup.dst_percentage() for roster in self.weekly_rosters])


	def avg_k_score(self):
		return numpy.mean([roster.active_lineup.k_score() for roster in self.weekly_rosters])


	def avg_k_percentage(self):
		return numpy.mean([roster.active_lineup.k_percentage() for roster in self.weekly_rosters])


	def calc_outcome(self, us, them):
		if us > them:
			return 'W'
		elif us < them:
			return 'L'
		else:
			return 'T'


	def print_summary(self, league):
		print self.team_name
		print self.owner_name
		print

		self.print_weekly_scoring_stats(league)

		self.print_weekly_position_breakdown()

# 		self.print_seasonal_stats(league)


	def print_weekly_scoring_stats(self, league):
		print 'Weekly Scoring Stats'
		print '--------------------'

		print '{:10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'.format('', 'Score', 'Optimal', 'Diff', 'Effic', 'Opp', 'Margin', 'Opp Effic', 'Result', 'Opt Result')
		for number, roster in zip(range(1, len(self.weekly_rosters) + 1), self.weekly_rosters):
			score = roster.active_score()
			optimal_score = roster.optimal_score()
			diff = score - optimal_score
			effic = float(score) / optimal_score * 100
			opp = league.teams[self.opponents[number - 1]].weekly_score(number)
			margin = score - opp
			opp_effic = league.teams[self.opponents[number - 1]].weekly_efficiency(number)
			outcome = self.calc_outcome(score, opp)
			optimal_outcome = self.calc_outcome(optimal_score, opp)
			print 'Week {:<5} {:<10} {:<10} {:<10} {:<10.2f} {:<10} {:<10} {:<10.2f} {:<10} {:<12}'.format(number, score, optimal_score, diff, effic, opp, margin, opp_effic, outcome, optimal_outcome)

		print '{:10} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10} {:<10}'.format('', self.avg_score(), self.avg_optimal_score(), self.avg_diff(), self.avg_efficiency(), self.avg_opp_score(league), self.avg_margin(league), self.avg_opp_efficiency(league), self.record(league), self.optimal_record(league))
		print


	def print_weekly_position_breakdown(self):
		print 'Weekly Positional Breakdown'
		print '---------------------------'

		print '{:10} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18}'.format('', 'QB', 'RB', 'WR', 'TE', 'FLEX', 'D/ST', 'K')
		for number, roster in zip(range(1, len(self.weekly_rosters) + 1), self.weekly_rosters):
			qb = '{:<6} ({:.2f})'.format(roster.active_lineup.qb_score(), roster.active_lineup.qb_percentage())
			rb = '{:<6} ({:.2f})'.format(roster.active_lineup.rb_score(), roster.active_lineup.rb_percentage())
			wr = '{:<6} ({:.2f})'.format(roster.active_lineup.wr_score(), roster.active_lineup.wr_percentage())
			te = '{:<6} ({:.2f})'.format(roster.active_lineup.te_score(), roster.active_lineup.te_percentage())
			flex = '{:<6} ({:.2f})'.format(roster.active_lineup.flex_score(), roster.active_lineup.flex_percentage())
			dst = '{:<6} ({:.2f})'.format(roster.active_lineup.dst_score(), roster.active_lineup.dst_percentage())
			k = '{:<6} ({:.2f})'.format(roster.active_lineup.k_score(), roster.active_lineup.k_percentage())
			print 'Week {:<5} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18}'.format(number, qb, rb, wr, te, flex, dst, k)

		qb = '{:<6.2f} ({:.2f})'.format(self.avg_qb_score(), self.avg_qb_percentage())
		rb = '{:<6.2f} ({:.2f})'.format(self.avg_rb_score(), self.avg_rb_percentage())
		wr = '{:<6.2f} ({:.2f})'.format(self.avg_wr_score(), self.avg_wr_percentage())
		te = '{:<6.2f} ({:.2f})'.format(self.avg_te_score(), self.avg_te_percentage())
		flex = '{:<6.2f} ({:.2f})'.format(self.avg_flex_score(), self.avg_flex_percentage())
		dst = '{:<6.2f} ({:.2f})'.format(self.avg_dst_score(), self.avg_dst_percentage())
		k = '{:<6.2f} ({:.2f})'.format(self.avg_k_score(), self.avg_k_percentage())
		print '{:10} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18}'.format('', qb, rb, wr, te, flex, dst, k)

		print '\n'


	def print_season_scoring_summary(self, league):
		print '{:10} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15} {:<15}'.format(self.short_name, self.avg_score(), self.avg_optimal_score(), self.avg_diff(), self.avg_efficiency(), self.avg_opp_score(league), self.avg_margin(league), self.avg_opp_efficiency(league), self.record(league), self.optimal_record(league))


	def print_weekly_scoring_summary(self, league, week):
		print '{:10} {:<15} {:<15} {:<15} {:<15.2f} {:<15} {:<15} {:<15.2f}'.format(self.short_name, self.weekly_score(week), self.weekly_optimal_score(week), self.weekly_diff(week), self.weekly_efficiency(week), self.weekly_opp_score(league, week), self.weekly_margin(league, week), self.weekly_opp_efficiency(league, week))


	def print_season_position_summary(self, league):
		qb = '{:<12.2f} ({:.2f})'.format(self.avg_qb_score(), self.avg_qb_percentage())
		rb = '{:<12.2f} ({:.2f})'.format(self.avg_rb_score(), self.avg_rb_percentage())
		wr = '{:<12.2f} ({:.2f})'.format(self.avg_wr_score(), self.avg_wr_percentage())
		te = '{:<12.2f} ({:.2f})'.format(self.avg_te_score(), self.avg_te_percentage())
		flex = '{:<12.2f} ({:.2f})'.format(self.avg_flex_score(), self.avg_flex_percentage())
		dst = '{:<12.2f} ({:.2f})'.format(self.avg_dst_score(), self.avg_dst_percentage())
		k = '{:<12.2f} ({:.2f})'.format(self.avg_k_score(), self.avg_k_percentage())
		print '{:10} {:<29} {:<29} {:<29} {:<29} {:<29} {:<29} {:<29}'.format(self.short_name, qb, rb, wr, te, flex, dst, k)


	def print_weekly_position_summary(self, league, week):
		qb = '{:<12} ({:.2f})'.format(self.weekly_rosters[week - 1].active_lineup.qb_score(), self.weekly_rosters[week - 1].active_lineup.qb_percentage())
		rb = '{:<12} ({:.2f})'.format(self.weekly_rosters[week - 1].active_lineup.rb_score(), self.weekly_rosters[week - 1].active_lineup.rb_percentage())
		wr = '{:<12} ({:.2f})'.format(self.weekly_rosters[week - 1].active_lineup.wr_score(), self.weekly_rosters[week - 1].active_lineup.wr_percentage())
		te = '{:<12} ({:.2f})'.format(self.weekly_rosters[week - 1].active_lineup.te_score(), self.weekly_rosters[week - 1].active_lineup.te_percentage())
		flex = '{:<12} ({:.2f})'.format(self.weekly_rosters[week - 1].active_lineup.flex_score(), self.weekly_rosters[week - 1].active_lineup.flex_percentage())
		dst = '{:<12} ({:.2f})'.format(self.weekly_rosters[week - 1].active_lineup.dst_score(), self.weekly_rosters[week - 1].active_lineup.dst_percentage())
		k = '{:<12} ({:.2f})'.format(self.weekly_rosters[week - 1].active_lineup.k_score(), self.weekly_rosters[week - 1].active_lineup.k_percentage())
		print '{:10} {:<29} {:<29} {:<29} {:<29} {:<29} {:<29} {:<29}'.format(self.short_name, qb, rb, wr, te, flex, dst, k)
