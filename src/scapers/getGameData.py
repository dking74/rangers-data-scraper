from bs4 import BeautifulSoup

from src.variables import boxscore_url
from src.loadHtml import loadHtml, loadTeamPlayerGameDataHtml, loadTeamScheduleHtml


def getTeamAndPlayerBatting(soup: BeautifulSoup):
  soup.select_one('#all_TexasRangersbatting')

def getTeamAndPlayerData(year_team_schedule_data: dict = None):
  '''Get team and player individual game batting data'''

  if year_team_schedule_data is None:
    year_team_schedule_data = loadTeamScheduleHtml()

  team_year_boxscore_mappings = {}
  # Go through each entry of soup content loaded from remote resource
  # and create a Coach entry found from within html
  for year, soup in year_team_schedule_data.items():
    team_year_boxscore_mappings[year] = {}
    boxscore_rows = soup.select('#all_team_schedule #div_team_schedule #team_schedule tbody tr')
    for boxscore_row in boxscore_rows:
      game_num_html = boxscore_row.select_one('th')
      game_number: str = game_num_html.text

      # If the game number is set as 'Gm#', the current
      # row is just a helper row in the set to establish what
      # the comments are. We should pass on from this.
      if game_number == 'Gm#':
        continue

      game_number = int(game_number)

      # Get the boxscore link and store that to the game number within current year
      boxscore_link = boxscore_url.format(
        box_link=boxscore_row.select_one('td[data-stat="boxscore"] a').attrs['href']
      )
      team_year_boxscore_mappings[year][game_number] = boxscore_link

  soup =loadHtml('https://www.baseball-reference.com/boxes/KCA/KCA202104010.shtml')
  # print(soup.select_one('#all_TexasRangersbatting'))
#   year_game_data = {}

#   year_game_mappings = loadTeamPlayerGameDataHtml(team_year_boxscore_mappings)
#   for year, game_data in year_game_mappings.items():
#     current_year_data = {
#       'batting': {
#         'team': {},
#         'players': {},
#       },
#       'pitching': {
#         'team': {},
#         'players': {},
#       }
#     }
#     for game_num, soup in game_data:
#       soup.select_one()