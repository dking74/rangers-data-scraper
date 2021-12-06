from src.loadHtml import loadTeamHomeHtml
from src.utility import replace_single_quote

def defaultBattingStats():
  return {
    'games': 0,
    'plate_appearances': 0,
    'at_bats': 0,
    'runs': 0,
    'hits': 0,
    'doubles': 0,
    'triples': 0,
    'home_runs': 0,
    'rbis': 0,
    'stolen_bases': 0,
    'caught_stealing': 0,
    'walks': 0,
    'strikeouts': 0,
    'batting_average': 0,
    'obp': 0,
    'slg': 0,
    'ops': 0,
    'ops_plus': 0,
    'total_bases': 0,
    'gdp': 0,
    'hbp': 0,
    'sacrifice_fly': 0,
    'ibb': 0
  }

def _loadBattingData(data_cols):
  '''Helper method to load batting data based on a row in data'''
  current_data = defaultBattingStats()
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

def getTeamAndPlayerBatDataByYear(year_team_home_data: dict = None) -> dict:
  '''
  Find the team and player bat data by year.
  '''

  if year_team_home_data is None:
    year_team_home_data = loadTeamHomeHtml()

  team_player_year_data = {}
  # Go through each entry of soup content loaded from remote resource
  # and create a Coach entry found from within html
  for year, soup in year_team_home_data.items():
    # Keep this entry to track stats for the team and players for the year
    team_player_year_entry = {
      'team': {},
      'players': {},
    }

    team_batting_container = soup.select('#all_team_batting #div_team_batting #team_batting')[0]
    team_batting_rows = team_batting_container.select('tbody tr:not(.thead)')
    for team_batting_row in team_batting_rows:
      current_player = {}
      player_name_td = team_batting_row.find('td', { 'data-stat': 'player' })
      player_name = replace_single_quote(player_name_td.find('a').text)
      # Determine if the player is already tracked. If not, create the entry
      # based on the player name and give the entry default stats.
      if player_name not in team_player_year_entry['players']:
        team_player_year_entry['players'][player_name] = {}

      remaining_data_cols = player_name_td.find_next_siblings()
      current_player = _loadBattingData(remaining_data_cols)
      team_player_year_entry['players'][player_name] = current_player
    
    # Load the data for team stats from the footer of the table
    team_stat_container = team_batting_container.find('tfoot')
    team_batting_row = team_stat_container.find('tr')
    team_batting_name_td = team_batting_row.find('td', { 'data-stat': 'player' })
    team_batting_stats_cols = team_batting_name_td.find_next_siblings()
    current_team_data = _loadBattingData(team_batting_stats_cols)
    team_player_year_entry['team'] = current_team_data

    # Store the team-player entry for specific year
    team_player_year_data[year] = team_player_year_entry

  return team_player_year_data