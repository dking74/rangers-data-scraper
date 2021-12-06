from src.loadHtml import loadTeamScheduleHtml
from src.utility.data_mappers import mapGameData
from src.utility.types_utils import setGameDefaults

def getGamesByYear(year_team_schedule_data: dict = None) -> dict:
  '''
  Create references to certain players to be saved in a dictionary to
  allow use by other player methods to get the players data attributes.
  '''

  if year_team_schedule_data is None:
    year_team_schedule_data = loadTeamScheduleHtml()

  year_game_data = {}
  for year, soup in year_team_schedule_data.items():
    game_data = {}
    game_rows = soup.select('#all_team_schedule #div_team_schedule #team_schedule tbody tr')
    for game_row in game_rows:
      game_num_html = game_row.select_one('th')
      game_number: str = game_num_html.text

      # If the game number is set as 'Gm#', the current
      # row is just a helper row in the set to establish what
      # the comments are. We should pass on from this.
      if game_number == 'Gm#':
        continue

      game_number = int(game_number)

      # Create a new game entry for storage and assign game_number
      # if the entry has not already been created.
      if game_number not in game_data:
        game_data[game_number] = {}

      game_data_vals = game_row.select('td')
      game_data = mapGameData(game_number, game_data_vals)
    year_game_data[year] = game_data

  return year_game_data