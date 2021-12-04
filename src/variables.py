from config import config

# Main config dictionaries
database_config = config()
variables_config = config('variables.ini', 'variables')

# Individual variables foudn in configs
years = variables_config['years'].split(' ')