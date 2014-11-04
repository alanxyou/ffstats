#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from ffteam import *


class League:
	def __init__(self, league_filename, file_stem):
		self.week_count = 0
		self.teams = {}

		self.import_league_info(league_filename, file_stem)


	def import_league_info(self, filename, stem):
		with open('{}/{}'.format(stem, filename)) as f:
			content = f.readlines()

			self.week_count = int(content[0].rstrip())

			for line in content[1:]:
				[short_name, team_name, owner_name] = line.rstrip().split('\t')
				self.teams[short_name] = Team(short_name, team_name, owner_name, self.week_count, stem)
	
	
	def print_scoring_summary(self):
		score = [self.teams[key].avg_score() for key in self.teams.keys()]
		optimal = [self.teams[key].avg_optimal_score() for key in self.teams.keys()]
		diff = [self.teams[key].avg_diff() for key in self.teams.keys()]
		effic = [self.teams[key].avg_efficiency() for key in self.teams.keys()]
		opp = [self.teams[key].avg_opp_score(self) for key in self.teams.keys()]
		margin = [self.teams[key].avg_margin(self) for key in self.teams.keys()]
		opp_effic = [self.teams[key].avg_opp_efficiency(self) for key in self.teams.keys()]
		
		score_str = '{:.2f} ±{:.2f}'.format(numpy.mean(score), numpy.std(score))
		optimal_str = '{:.2f} ±{:.2f}'.format(numpy.mean(optimal), numpy.std(optimal))
		diff_str = '{:.2f} ±{:.2f}'.format(numpy.mean(diff), numpy.std(diff))
		effic_str = '{:.2f} ±{:.2f}'.format(numpy.mean(effic), numpy.std(effic))
		opp_str = '{:.2f} ±{:.2f}'.format(numpy.mean(opp), numpy.std(opp))
		margin_str = '{:.2f} ±{:.2f}'.format(numpy.mean(margin), numpy.std(margin))
		effic_str = '{:.2f} ±{:.2f}'.format(numpy.mean(opp_effic), numpy.std(opp_effic))
		
		print '{:10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format('', 'Score', 'Optimal', 'Diff', 'Effic', 'Opp', 'Margin', 'Opp Effic', 'Record', 'Opt Record')
		for key in sorted(self.teams.keys()):
			self.teams[key].print_season_scoring_summary(self)
			
		print '{:10} {:<16} {:<16} {:<16} {:<16} {:<16} {:<16} {:<16}'.format('', score_str, optimal_str, diff_str, effic_str, opp_str, margin_str, effic_str)

	
	
	def print_weekly_scoring_summary(self, week):
		score = [self.teams[key].weekly_score(week) for key in self.teams.keys()]
		optimal = [self.teams[key].weekly_optimal_score(week) for key in self.teams.keys()]
		diff = [self.teams[key].weekly_diff(week) for key in self.teams.keys()]
		effic = [self.teams[key].weekly_efficiency(week) for key in self.teams.keys()]
		opp = [self.teams[key].weekly_opp_score(self, week) for key in self.teams.keys()]
		margin = [self.teams[key].weekly_margin(self, week) for key in self.teams.keys()]
		opp_effic = [self.teams[key].weekly_opp_efficiency(self, week) for key in self.teams.keys()]
		
		score_str = '{:.2f} ±{:.2f}'.format(numpy.mean(score), numpy.std(score))
		optimal_str = '{:.2f} ±{:.2f}'.format(numpy.mean(optimal), numpy.std(optimal))
		diff_str = '{:.2f} ±{:.2f}'.format(numpy.mean(diff), numpy.std(diff))
		effic_str = '{:.2f} ±{:.2f}'.format(numpy.mean(effic), numpy.std(effic))
		opp_str = '{:.2f} ±{:.2f}'.format(numpy.mean(opp), numpy.std(opp))
		margin_str = '{:.2f} ±{:.2f}'.format(numpy.mean(margin), numpy.std(margin))
		effic_str = '{:.2f} ±{:.2f}'.format(numpy.mean(opp_effic), numpy.std(opp_effic))
		
		print '{:10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format('', 'Score', 'Optimal', 'Difference', 'Efficiency', 'Opp', 'Margin', 'Opp Efficiency')
		for key in sorted(self.teams.keys()):
			self.teams[key].print_weekly_scoring_summary(self, week)
			
		print '{:10} {:<16} {:<16} {:<16} {:<16} {:<16} {:<16} {:<16}'.format('', score_str, optimal_str, diff_str, effic_str, opp_str, margin_str, effic_str)
	
	
	def print_position_summary(self):
		qb = [self.teams[key].avg_qb_score() for key in self.teams.keys()]
		rb = [self.teams[key].avg_rb_score() for key in self.teams.keys()]
		wr = [self.teams[key].avg_wr_score() for key in self.teams.keys()]
		te = [self.teams[key].avg_te_score() for key in self.teams.keys()]
		flex = [self.teams[key].avg_flex_score() for key in self.teams.keys()]
		dst = [self.teams[key].avg_dst_score() for key in self.teams.keys()]
		k = [self.teams[key].avg_k_score() for key in self.teams.keys()]

		qb_per = [self.teams[key].avg_qb_percentage() for key in self.teams.keys()]
		rb_per = [self.teams[key].avg_rb_percentage() for key in self.teams.keys()]
		wr_per = [self.teams[key].avg_wr_percentage() for key in self.teams.keys()]
		te_per = [self.teams[key].avg_te_percentage() for key in self.teams.keys()]
		flex_per = [self.teams[key].avg_flex_percentage() for key in self.teams.keys()]
		dst_per = [self.teams[key].avg_dst_percentage() for key in self.teams.keys()]
		k_per = [self.teams[key].avg_k_percentage() for key in self.teams.keys()]
		
		qb_str = '{:<14}{:<17}'.format('{:<.2f} ±{:<.2f}'.format(numpy.mean(qb), numpy.std(qb)), '({:<.2f} ±{:<.2f})'.format(numpy.mean(qb_per), numpy.std(qb_per)))
		rb_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(rb), numpy.std(rb)), '({:.2f} ±{:.2f})'.format(numpy.mean(rb_per), numpy.std(rb_per)))
		wr_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(wr), numpy.std(wr)), '({:.2f} ±{:.2f})'.format(numpy.mean(wr_per), numpy.std(wr_per)))
		te_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(te), numpy.std(te)), '({:.2f} ±{:.2f})'.format(numpy.mean(te_per), numpy.std(te_per)))
		flex_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(flex), numpy.std(flex)), '({:.2f} ±{:.2f})'.format(numpy.mean(flex_per), numpy.std(flex_per)))
		dst_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(dst), numpy.std(dst)), '({:.2f} ±{:.2f})'.format(numpy.mean(dst_per), numpy.std(dst_per)))
		k_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(k), numpy.std(k)), '({:.2f} ±{:.2f})'.format(numpy.mean(k_per), numpy.std(k_per)))
		
		print '{:10} {:<29} {:<29} {:<29} {:<29} {:<29} {:<29} {:<29}'.format('', 'QB', 'RB', 'WR', 'TE', 'FLEX', 'D/ST', 'K')
		for key in sorted(self.teams.keys()):
			self.teams[key].print_season_position_summary(self)

		print '{:10} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18}'.format('', qb_str, rb_str, wr_str, te_str, flex_str, dst_str, k_str)
				
	
	def print_weekly_position_summary(self, week):
		qb = [self.teams[key].weekly_rosters[week - 1].active_lineup.qb_score() for key in self.teams.keys()]
		rb = [self.teams[key].weekly_rosters[week - 1].active_lineup.rb_score() for key in self.teams.keys()]
		wr = [self.teams[key].weekly_rosters[week - 1].active_lineup.wr_score() for key in self.teams.keys()]
		te = [self.teams[key].weekly_rosters[week - 1].active_lineup.te_score() for key in self.teams.keys()]
		flex = [self.teams[key].weekly_rosters[week - 1].active_lineup.flex_score() for key in self.teams.keys()]
		dst = [self.teams[key].weekly_rosters[week - 1].active_lineup.dst_score() for key in self.teams.keys()]
		k = [self.teams[key].weekly_rosters[week - 1].active_lineup.k_score() for key in self.teams.keys()]

		qb_per = [self.teams[key].weekly_rosters[week - 1].active_lineup.qb_percentage() for key in self.teams.keys()]
		rb_per = [self.teams[key].weekly_rosters[week - 1].active_lineup.rb_percentage() for key in self.teams.keys()]
		wr_per = [self.teams[key].weekly_rosters[week - 1].active_lineup.wr_percentage() for key in self.teams.keys()]
		te_per = [self.teams[key].weekly_rosters[week - 1].active_lineup.te_percentage() for key in self.teams.keys()]
		flex_per = [self.teams[key].weekly_rosters[week - 1].active_lineup.flex_percentage() for key in self.teams.keys()]
		dst_per = [self.teams[key].weekly_rosters[week - 1].active_lineup.dst_percentage() for key in self.teams.keys()]
		k_per = [self.teams[key].weekly_rosters[week - 1].active_lineup.k_percentage() for key in self.teams.keys()]
		
		qb_str = '{:<14}{:<17}'.format('{:<.2f} ±{:<.2f}'.format(numpy.mean(qb), numpy.std(qb)), '({:<.2f} ±{:<.2f})'.format(numpy.mean(qb_per), numpy.std(qb_per)))
		rb_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(rb), numpy.std(rb)), '({:.2f} ±{:.2f})'.format(numpy.mean(rb_per), numpy.std(rb_per)))
		wr_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(wr), numpy.std(wr)), '({:.2f} ±{:.2f})'.format(numpy.mean(wr_per), numpy.std(wr_per)))
		te_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(te), numpy.std(te)), '({:.2f} ±{:.2f})'.format(numpy.mean(te_per), numpy.std(te_per)))
		flex_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(flex), numpy.std(flex)), '({:.2f} ±{:.2f})'.format(numpy.mean(flex_per), numpy.std(flex_per)))
		dst_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(dst), numpy.std(dst)), '({:.2f} ±{:.2f})'.format(numpy.mean(dst_per), numpy.std(dst_per)))
		k_str = '{:<14}{:<17}'.format('{:.2f} ±{:.2f}'.format(numpy.mean(k), numpy.std(k)), '({:.2f} ±{:.2f})'.format(numpy.mean(k_per), numpy.std(k_per)))
		
		print '{:10} {:<29} {:<29} {:<29} {:<29} {:<29} {:<29} {:<29}'.format('', 'QB', 'RB', 'WR', 'TE', 'FLEX', 'D/ST', 'K')
		for key in sorted(self.teams.keys()):
			self.teams[key].print_weekly_position_summary(self, week)
			
		print '{:10} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18}'.format('', qb_str, rb_str, wr_str, te_str, flex_str, dst_str, k_str)
