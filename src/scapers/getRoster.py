from src.loadHtml import loadTeamRosterHtml
from src.utility.data_mappers import mapRosterData
from src.utility.string_utils import replace_single_quote
from src.utility.types_utils import setPlayerDefaults

def getPlayersByYear(year_team_roster_data: dict = None) -> dict:
  '''
  Create references to certain players to be saved in a dictionary to
  allow use by other player methods to get the players data attributes.
  '''

  if year_team_roster_data is None:
    year_team_roster_data = loadTeamRosterHtml()

  # Go through each entry of soup content loaded from remote resource
  # and create a Player entry found from within html
  player_roster_data = {}
  for year, soup in year_team_roster_data.items():
    players_data = {}
    players_rows = soup.select('#all_appearances #div_appearances #appearances tbody tr')
    for player_row in players_rows:
      player_name_html = player_row.select_one('th a')
      player_name: str = replace_single_quote(player_name_html.contents[0])

      # Create a new player entry for storage and assign name
      # if the entry has not already been created.
      if player_name not in players_data:
        players_data[player_name] = {}

      player_data = player_row.select('td')
      players_data[player_name] = mapRosterData(player_name, player_data)
    player_roster_data[year] = players_data

  return player_roster_data