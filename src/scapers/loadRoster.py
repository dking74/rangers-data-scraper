from readHtml import loadHtml
from variables import years

def loadPlayers() -> dict:
  '''
  Create references to certain players to be saved in a dictionary to
  allow use by other player methods to get the players data attributes.
  '''

  players_data = {}
  for year in years:
    current_html_url = 'https://www.baseball-reference.com/teams/TEX/{}-roster.shtml'.format(year)
    soup = loadHtml(current_html_url)
    players_rows = soup.select('#all_appearances #div_appearances #appearances tbody tr')
    for player_row in players_rows:
      player_name_html = player_row.select_one('th a')
      player_name = player_name_html.contents[0]

      # Create a new player entry for storage and assign name
      # if the entry has not already been created.
      if player_name not in players_data:
        players_data[player_name] = { 'name': player_name }

      player_data = player_row.select('td')
      for data_td in player_data:
        data_stat = data_td.attrs['data-stat']
        
        # Look at individal td elements and determine if they correspond
        # with the metadata elements we care about for players. Store those
        # metadata values accordingly for later usage.
        if data_stat == 'age':
          players_data[player_name]['age'] = data_td.text
        if data_stat == 'flag' and len(data_td.contents) > 1:
          players_data[player_name]['country'] = str(data_td.contents[1]).strip()
        if data_stat == 'bats':
          players_data[player_name]['bats'] = data_td.text
        if data_stat == 'throws':
          players_data[player_name]['throws'] = data_td.text
        if data_stat == 'height':
          players_data[player_name]['height'] = data_td.text
        if data_stat == 'weight':
          players_data[player_name]['weight'] = data_td.text
        if data_stat == 'date_of_birth':
          players_data[player_name]['dob'] = data_td.attrs['csk']
        if data_stat == 'experience':
          players_data[player_name]['years'] = data_td.attrs['csk']

  return players_data


# def loadCoachingStaff():