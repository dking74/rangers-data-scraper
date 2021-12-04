from readHtml import loadHtml
from variables import years

def loadPlayerData():
  '''
  Load the html for a specific player and set their player performance data
  '''

#   players_data = loadPlayersReferences()
  # base_url = 'https://www.baseball-reference.com'
  # for player_data in players_data.values():
  #   player_link = player_data['link']
  #   current_html_page = '{base_url}{player_link}'.format(base_url=base_url, player_link=player_link)
  #   player_html = loadHtml(current_html_page)

  #   # Get Logo for player
  #   player_img = player_html.select_one('#info.players #meta .media-item.multiple img')
  #   if player_img is not None:
  #     players_data[player_data['name']] = player_img.get('src')