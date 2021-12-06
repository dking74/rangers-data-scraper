from src.loadHtml import loadTeamHomeHtml
from src.utility.string_utils import replace_single_quote
from src.utility.data_mappers import mapBattingData, mapPitchingData

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
      current_player = mapBattingData(remaining_data_cols)
      team_player_year_entry['players'][player_name] = current_player
    
    # Load the data for team stats from the footer of the table
    team_stat_container = team_batting_container.find('tfoot')
    team_batting_row = team_stat_container.find('tr')
    team_batting_name_td = team_batting_row.find('td', { 'data-stat': 'player' })
    team_batting_stats_cols = team_batting_name_td.find_next_siblings()
    current_team_data = mapBattingData(team_batting_stats_cols)
    team_player_year_entry['team'] = current_team_data

    # Store the team-player entry for specific year
    team_player_year_data[year] = team_player_year_entry

  return team_player_year_data

def getTeamAndPlayerPitchDataByYear(year_team_home_data: dict = None) -> dict:
  '''
  Find the team and player pitching data by year.
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

    team_pitching_container = soup.select('#all_team_pitching #div_team_pitching #team_pitching')[0]
    team_pitching_rows = team_pitching_container.select('tbody tr:not(.thead)')
    for team_pitching_row in team_pitching_rows:
      current_player = {}
      player_name_td = team_pitching_row.find('td', { 'data-stat': 'player' })
      player_name = replace_single_quote(player_name_td.find('a').text)
      # Determine if the player is already tracked. If not, create the entry
      # based on the player name and give the entry default stats.
      if player_name not in team_player_year_entry['players']:
        team_player_year_entry['players'][player_name] = {}

      remaining_data_cols = player_name_td.find_next_siblings()
      current_player = mapPitchingData(remaining_data_cols)
      team_player_year_entry['players'][player_name] = current_player
    
    # Load the data for team stats from the footer of the table
    team_stat_container = team_pitching_container.find('tfoot')
    team_pitching_row = team_stat_container.find('tr')
    team_pitching_name_td = team_pitching_row.find('td', { 'data-stat': 'player' })
    team_pitching_stats_cols = team_pitching_name_td.find_next_siblings()
    current_team_data = mapPitchingData(team_pitching_stats_cols)
    team_player_year_entry['team'] = current_team_data

    # Store the team-player entry for specific year
    team_player_year_data[year] = team_player_year_entry

  return team_player_year_data