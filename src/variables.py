from src.config import config

# Main config dictionaries
database_config = config()
variables_config = config('variables.ini', 'variables')

# Individual variables foudn in configs
years = variables_config['years'].split(' ')

team_base_url = 'https://www.baseball-reference.com/teams/TEX'
team_home_url = team_base_url + '/{year}.shtml'
team_roster_url = team_base_url + '/{year}-roster.shtml'