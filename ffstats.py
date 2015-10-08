#!/usr/local/bin/python

from ffleague import *


FILE_STEM = '/Users/Alan/Dropbox/Developer/ffstats'


league = League('league_info.txt', FILE_STEM)


print '=============='
print 'LEAGUE SUMMARY'
print '=============='
print

print 'Scoring Summary'
print '---------------'

league.print_scoring_summary()

print '\n'
print 'Positional Summary'
print '------------------'

league.print_position_summary()

print '\n\n'
print '=============='
print 'TEAM SUMMARIES'
print '=============='
print

for owner in sorted(league.teams.keys()):
	league.teams[owner].print_summary(league)

print 
print '================'
print 'WEEKLY SUMMARIES'
print '================'
print

for index in range(1, league.week_count + 1):
	print 'Week {:<2} Scoring Summary'.format(index)
	print '-----------------------'
	
	league.print_weekly_scoring_summary(index)
	
	print '\n'
	print 'Week {:<2} Positional Summary'.format(index)
	print '--------------------------'
	
	league.print_weekly_position_summary(index)
	
	print '\n'
