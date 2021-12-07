from src.config import config

# Main config dictionaries
database_config = config()
variables_config = config('variables.ini', 'variables')

# Individual variables foudn in configs
years = variables_config['years'].split(' ')

baseball_reference_url = 'https://www.baseball-reference.com'
boxscore_url = baseball_reference_url + '{box_link}'
team_base_url = '{0}/teams/TEX'.format(baseball_reference_url)
team_home_url = team_base_url + '/{year}.shtml'
team_roster_url = team_base_url + '/{year}-roster.shtml'
team_schedule_url = team_base_url + '/{year}-schedule-scores.shtml'
team_fielding_url = team_base_url + '/{year}-fielding.shtml'