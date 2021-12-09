from src.utility.string_utils import replace_whitespace, replace_single_quote
from src.utility.types_utils import setBattingStatsDefaults, setFieldingStatsDefaults, setGameDefaults, setPitchingStatsDefaults, setPlayerDefaults

def mapGameData(game_number: int, game_data_vals: list):
  game_data = setGameDefaults(game_number)
  for data_td in game_data_vals:
    data_stat = data_td.attrs['data-stat']
        
    # Map the stat values to database values that need to
    # be inserted in our own database
    if data_stat == 'date_game':
      date = data_td.attrs['csk']
      month = int(date.split('-')[1]) if date else ''
      game_data['date'] = date
      game_data['month'] = month
    if data_stat == 'opp_ID':
      opponent_link = data_td.find('a')
      game_data['opponent'] = opponent_link.text \
      if opponent_link is not None else data_td.text
    if data_stat == 'homeORvis':
      home_or_away = data_td.text
      game_data['home_or_away'] = 'home' \
    if home_or_away or home_or_away != '@' else 'away'
    if data_stat == 'win_loss_result':
      game_data['result'] = data_td.text[0] if len(data_td.text) > 0 else 'W'
    if data_stat =='extra_innings':
      game_data['innings'] = int(data_td.text) \
      if data_td.text else 9
    if data_stat == 'win_loss_record':
      record = data_td.text.split('-')
      game_data['team_wins_after'] = record[0]
      game_data['team_losses_after'] = record[1]
    if data_stat == 'winning_pitcher':
      pitcher_link = data_td.find('a')
      game_data['winning_pitcher'] = \
      replace_single_quote(replace_whitespace(pitcher_link.attrs['title'])) \
      if pitcher_link is not None else data_td.text
    if data_stat == 'losing_pitcher':
      pitcher_link = data_td.find('a')
      game_data['losing_pitcher'] = \
      replace_single_quote(replace_whitespace(pitcher_link.attrs['title'])) \
      if pitcher_link is not None else data_td.text
    if data_stat == 'saving_pitcher':
      pitcher_link = data_td.find('a')
      game_data['saving_pitcher'] = \
      replace_single_quote(replace_whitespace(pitcher_link.attrs['title'])) \
      if pitcher_link is not None else ''
    if data_stat == 'attendance':
      attendance = data_td.text
      game_data['attendance'] = int(attendance.replace(',', '')) \
      if attendance else 0
    if data_stat == 'time_of_game':
      game_data['time'] = data_td.text or '00:00'

  return game_data

def mapRosterData(player_name: str, player_data: list):
  # Set the default of the dict and then map the entries
  names = player_name.split(' ')
  first_name = names[0]
  last_name = names[1]
  players_data = setPlayerDefaults(first_name, last_name)

  for data_td in player_data:
    data_stat = data_td.attrs['data-stat']

    # Look at individal td elements and determine if they correspond
    # with the metadata elements we care about for players. Store those
    # metadata values accordingly for later usage.
    if data_stat == 'age':
      players_data['age'] = int(data_td.text)
    if data_stat == 'flag' and len(data_td.contents) > 1:
      players_data['country'] = str(data_td.contents[1]).strip()
    if data_stat == 'bats':
      bats = data_td.text
      if bats == 'B': bats = 'S'
      if bats != 'R' or bats != 'L': bats = 'R'
      players_data['bats'] = bats
    if data_stat == 'throws':
      throws = data_td.text
      if throws == 'B': throws = 'S'
      if throws != 'R' or throws != 'L': throws = 'R'
      players_data['throws'] = throws
    if data_stat == 'height':
      players_data['height'] = str(data_td.text).replace("'", "''")
    if data_stat == 'weight':
      players_data['weight'] = int(data_td.text)
    if data_stat == 'date_of_birth':
      players_data['dob'] = data_td.attrs['csk']
    if data_stat == 'experience':
      players_data['years'] = int(data_td.attrs['csk'])

  return players_data

def mapBattingData(data_cols: list):
  '''Helper method to load batting data based on a row in data'''
  current_data = setBattingStatsDefaults()
  for data_col in data_cols:
    stat = data_col.attrs['data-stat']

    if stat == 'G':
      current_data['games'] = int(data_col.text) if data_col.text else 0
    if stat == 'PA':
      current_data['plate_appearances'] = int(data_col.text) if data_col.text else 0
    if stat == 'AB':
      current_data['at_bats'] = int(data_col.text) if data_col.text else 0
    if stat == 'R':
      current_data['runs'] = int(data_col.text) if data_col.text else 0
    if stat == 'H':
      current_data['hits'] = int(data_col.text) if data_col.text else 0
    if stat == '2B':
      current_data['doubles'] = int(data_col.text) if data_col.text else 0
    if stat == '3B':
      current_data['triples'] = int(data_col.text) if data_col.text else 0
    if stat == 'HR':
      current_data['home_runs'] = int(data_col.text) if data_col.text else 0
    if stat == 'RBI':
      current_data['rbis'] = int(data_col.text) if data_col.text else 0
    if stat == 'SB':
      current_data['stolen_bases'] = int(data_col.text) if data_col.text else 0
    if stat == 'CS':
      current_data['caught_stealing'] = int(data_col.text) if data_col.text else 0
    if stat == 'BB':
      current_data['walks'] = int(data_col.text) if data_col.text else 0
    if stat == 'SO':
      current_data['strikeouts'] = int(data_col.text) if data_col.text else 0
    if stat == 'batting_avg':
      current_data['batting_average'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'onbase_perc':
      current_data['obp'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'slugging_perc':
      current_data['slg'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'onbase_plus_slugging':
      current_data['ops'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'onbase_plus_slugging_plus':
      current_data['ops_plus'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'TB':
      current_data['total_bases'] = int(data_col.text) if data_col.text else 0
    if stat == 'GIDP':
      current_data['gdp'] = int(data_col.text) if data_col.text else 0
    if stat == 'HBP':
      current_data['hbp'] = int(data_col.text) if data_col.text else 0
    if stat == 'SF':
      current_data['sacrifice_fly'] = int(data_col.text) if data_col.text else 0
    if stat == 'IBB':
      current_data['ibb'] = int(data_col.text) if data_col.text else 0

  return current_data

def mapPitchingData(data_cols: list):
  '''Helper method to load pitching data based on a row in data'''
  current_data = setPitchingStatsDefaults()
  for data_col in data_cols:
    stat = data_col.attrs['data-stat']

    if stat == 'W':
      current_data['wins'] = int(data_col.text) if data_col.text else 0
    if stat == 'L':
      current_data['losses'] = int(data_col.text) if data_col.text else 0
    if stat == 'win_loss_perc':
      current_data['win_percentage'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'earned_run_avg':
      current_data['era'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'G':
      current_data['games'] = int(data_col.text) if data_col.text else 0
    if stat == 'GS':
      current_data['games_started'] = int(data_col.text) if data_col.text else 0
    if stat == 'GF':
      current_data['games_finished'] = int(data_col.text) if data_col.text else 0
    if stat == 'CG':
      current_data['complete_games'] = int(data_col.text) if data_col.text else 0
    if stat == 'SHO':
      current_data['shutouts'] = int(data_col.text) if data_col.text else 0
    if stat == 'SV':
      current_data['saves'] = int(data_col.text) if data_col.text else 0
    if stat == 'IP':
      current_data['innings_pitched'] = float(data_col.text) if data_col.text else float('0.0')
    if stat == 'H':
      current_data['hits'] = int(data_col.text) if data_col.text else 0
    if stat == 'R':
      current_data['runs'] = int(data_col.text) if data_col.text else 0
    if stat == 'ER':
      current_data['earned_runs'] = int(data_col.text) if data_col.text else 0
    if stat == 'HR':
      current_data['home_runs'] = int(data_col.text) if data_col.text else 0
    if stat == 'BB':
      current_data['walks'] = int(data_col.text) if data_col.text else 0
    if stat == 'IBB':
      current_data['intentional_walks'] = int(data_col.text) if data_col.text else 0
    if stat == 'SO':
      current_data['strikeouts'] = int(data_col.text) if data_col.text else 0
    if stat == 'HBP':
      current_data['hbp'] = int(data_col.text) if data_col.text else 0
    if stat == 'BK':
      current_data['balks'] = int(data_col.text) if data_col.text else 0
    if stat == 'WP':
      current_data['wild_pitches'] = int(data_col.text) if data_col.text else 0
    if stat == 'batters_faced':
      current_data['batters_faced'] = int(data_col.text) if data_col.text else 0
    if stat == 'earned_run_avg_plus':
      current_data['era_plus'] = int(data_col.text) if data_col.text else 0
    if stat == 'fip':
      current_data['fip'] = float(data_col.text) if data_col.text else float('0.00')
    if stat == 'whip':
      current_data['whip'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'hits_per_nine':
      current_data['hits_per_9'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'bases_on_balls_per_nine':
      current_data['bb_per_9'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'strikeouts_per_nine':
      current_data['k_per_9'] = float(data_col.text) if data_col.text else float('0.000')

  return current_data

def mapFieldingData(data_cols: list):
  '''Helper method to load fielding data based on a row in data'''
  current_data = setFieldingStatsDefaults()
  for data_col in data_cols:
    stat = data_col.attrs['data-stat']

    if stat == 'G':
      current_data['games'] = int(data_col.text) if data_col.text else 0
    if stat == 'GS':
      current_data['games_started'] = int(data_col.text) if data_col.text else 0
    if stat == 'Inn_def':
      current_data['innings'] = float(data_col.text) if data_col.text else float('0.0')
    if stat == 'chances':
      current_data['chances'] = int(data_col.text) if data_col.text else 0
    if stat == 'PO':
      current_data['putouts'] = int(data_col.text) if data_col.text else 0
    if stat == 'A':
      current_data['assists'] = int(data_col.text) if data_col.text else 0
    if stat == 'E_def':
      current_data['errors'] = int(data_col.text) if data_col.text else 0
    if stat == 'DP_def':
      current_data['double_plays'] = int(data_col.text) if data_col.text else 0
    if stat == 'fielding_perc':
      current_data['fielding_percentage'] = float(data_col.text) if data_col.text else float('0.000')
    if stat == 'bis_runs_total':
      current_data['drs'] = float(data_col.text) if data_col.text else float('0.00')
    if stat == 'bis_runs_total_per_season':
      current_data['drs_per_year'] = float(data_col.text) if data_col.text else float('0.00')
  return current_data