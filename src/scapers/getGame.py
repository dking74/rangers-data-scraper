from src.loadHtml import loadTeamScheduleHtml
from src.utility.string_utils import replace_whitespace, replace_single_quote

def setGameDefaults(game_number: int):
  return {
    'game_number': game_number,
    'date': '',
    'month': 1,
    'opponent': '',
    'home_or_away': 'home',
    'innings': 9,
    'result': 'W',
    'team_wins_after': 0,
    'team_losses_after': 0,
    'time': '00:00',
    'attendance': 0,
    'winning_pitcher': '',
    'losing_pitcher': '',
    'saving_pitcher': '',
  }

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

      # Create a new game entry for storage and assign game_number
      # if the entry has not already been created.
      if game_number not in game_data:
        game_data[game_number] = setGameDefaults(int(game_number))

      game_data_vals = game_row.select('td')
      for data_td in game_data_vals:
        data_stat = data_td.attrs['data-stat']
        
        # Map the stat values to database values that need to
        # be inserted in our own database
        if data_stat == 'date_game':
          date = data_td.attrs['csk']
          month = int(date.split('-')[1]) if date else ''
          game_data[game_number]['date'] = date
          game_data[game_number]['month'] = month
        if data_stat == 'opp_ID':
          opponent_link = data_td.find('a')
          game_data[game_number]['opponent'] = opponent_link.text \
            if opponent_link is not None else data_td.text
        if data_stat == 'homeORvis':
          home_or_away = data_td.text
          game_data[game_number]['home_or_away'] = 'home' \
            if home_or_away or home_or_away != '@' else 'away'
        if data_stat == 'win_loss_result':
          game_data[game_number]['result'] = data_td.text[0] if len(data_td.text) > 0 else 'W'
        if data_stat =='extra_innings':
          game_data[game_number]['innings'] = int(data_td.text) \
            if data_td.text else 9
        if data_stat == 'win_loss_record':
          record = data_td.text.split('-')
          game_data[game_number]['team_wins_after'] = record[0]
          game_data[game_number]['team_losses_after'] = record[1]
        if data_stat == 'winning_pitcher':
          pitcher_link = data_td.find('a')
          game_data[game_number]['winning_pitcher'] = \
            replace_single_quote(replace_whitespace(pitcher_link.attrs['title'])) \
            if pitcher_link is not None else data_td.text
        if data_stat == 'losing_pitcher':
          pitcher_link = data_td.find('a')
          game_data[game_number]['losing_pitcher'] = \
            replace_single_quote(replace_whitespace(pitcher_link.attrs['title'])) \
            if pitcher_link is not None else data_td.text
        if data_stat == 'saving_pitcher':
          pitcher_link = data_td.find('a')
          game_data[game_number]['saving_pitcher'] = \
            replace_single_quote(replace_whitespace(pitcher_link.attrs['title'])) \
            if pitcher_link is not None else ''
        if data_stat == 'attendance':
          attendance = data_td.text
          game_data[game_number]['attendance'] = int(attendance.replace(',', '')) \
            if attendance else 0
        if data_stat == 'time_of_game':
          game_data[game_number]['time'] = data_td.text or '00:00'
    year_game_data[year] = game_data

  return year_game_data