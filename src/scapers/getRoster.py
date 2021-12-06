from src.loadHtml import loadTeamRosterHtml
from src.utility import replace_single_quote

def setPlayerDefaults(first_name: str = '', last_name: str = ''):
  return {
    'first_name': first_name,
    'last_name': last_name,
    'age': '',
    'country': 'US',
    'bats': 'R',
    'throws': 'R',
    'height': '',
    'weight': 0,
    'dob': '',
    'years': 0,
    'logo': '',
    'position': ''
  }

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
        names = player_name.split(' ')
        first_name = names[0]
        last_name = names[1]
        players_data[player_name] = setPlayerDefaults(first_name, last_name)

      player_data = player_row.select('td')
      for data_td in player_data:
        data_stat = data_td.attrs['data-stat']
        
        # Look at individal td elements and determine if they correspond
        # with the metadata elements we care about for players. Store those
        # metadata values accordingly for later usage.
        if data_stat == 'age':
          players_data[player_name]['age'] = int(data_td.text)
        if data_stat == 'flag' and len(data_td.contents) > 1:
          players_data[player_name]['country'] = str(data_td.contents[1]).strip()
        if data_stat == 'bats':
          bats = data_td.text
          if bats == 'B': bats = 'S'
          if bats != 'R' or bats != 'L': bats = 'R'
          players_data[player_name]['bats'] = bats
        if data_stat == 'throws':
          throws = data_td.text
          if throws == 'B': throws = 'S'
          if throws != 'R' or throws != 'L': throws = 'R'
          players_data[player_name]['throws'] = throws
        if data_stat == 'height':
          players_data[player_name]['height'] = str(data_td.text).replace("'", "''")
        if data_stat == 'weight':
          players_data[player_name]['weight'] = int(data_td.text)
        if data_stat == 'date_of_birth':
          players_data[player_name]['dob'] = data_td.attrs['csk']
        if data_stat == 'experience':
          players_data[player_name]['years'] = int(data_td.attrs['csk'])

    player_roster_data[year] = players_data
  return player_roster_data