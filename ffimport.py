#!/usr/local/bin/python

import lxml.html

FILE_STEM = '/Users/Alan/Dropbox/Developer/ffstats'
URL_STEM = 'http://games.espn.go.com/ffl/boxscorequick?leagueId={}&teamId={}&scoringPeriodId={}&seasonId={}&view=scoringperiod&version=quick'
NUM_TEAMS = 12
LEAGUE_ID = 1108509
SEASON_ID = 2015


def generate_score_sheet(doc):
	output = []

	starters = doc.xpath("//table[@id='playertable_0']")[0]
	bench = doc.xpath("//table[@id='playertable_1']")[0]

	for player in starters.xpath(".//tr[contains(concat(' ', @class, ' '), ' pncPlayerRow ')]"):
		name = player.xpath(".//td[contains(concat(' ', @class, ' '), ' playertablePlayerName ')]/a/text()")[0]
		position = str(player.xpath(".//td[contains(concat(' ', @class, ' '), ' playertablePlayerName ')]/text()")[0].replace(u'\xa0', u' ')).rstrip().split(' ')[-1]
		slot = player.xpath(".//td[contains(concat(' ', @class, ' '), ' playerSlot ')]/text()")[0]
		points = player.xpath(".//td[contains(concat(' ', @class, ' '), ' appliedPoints ')]/text()")[0]

		output.append('\t'.join([name, position, slot, points]))

	for player in bench.xpath(".//tr[contains(concat(' ', @class, ' '), ' pncPlayerRow ')]")[:-1]:
		if len(player.xpath(".//td[contains(concat(' ', @class, ' '), ' playertablePlayerName ')]/a/text()")) == 0:
			continue
		
		name = player.xpath(".//td[contains(concat(' ', @class, ' '), ' playertablePlayerName ')]/a/text()")[0]
		position = str(player.xpath(".//td[contains(concat(' ', @class, ' '), ' playertablePlayerName ')]/text()")[0].replace(u'\xa0', u' ')).rstrip().split(' ')[-1]
		slot = 'BE'
		points = player.xpath(".//td[contains(concat(' ', @class, ' '), ' appliedPoints ')]/text()")[0]

		if points == '--':
			points = '0'

		output.append('\t'.join([name, position, slot, points]))

	return '\n'.join(output)

# Main Body
week_count = 0
teams = {}

# Import league information
with open('{}/{}'.format(FILE_STEM, 'league_info.txt')) as f:
	content = f.readlines()

	week_count = int(content[0].rstrip())

	for line in content[1:]:
		[team_id, short_name, team_name, owner_name] = line.rstrip().split('\t')
		teams[team_id] = short_name

for week in range(1, week_count + 1):
	for (team_id, team) in teams.iteritems():
		output_filename = '{}/teams/{}/{}_{}.txt'.format(FILE_STEM, team, team, week)
		score_url = URL_STEM.format(LEAGUE_ID, team_id, week, SEASON_ID)

		print 'Generating Scores Sheet for {} week {}'.format(team, week)

		outputfile = open(output_filename, 'w')
		doc = lxml.html.parse(score_url)

		outputfile.write(generate_score_sheet(doc))

		outputfile.close()
