def getGameIdByYearAndGameNumQuery(year: int, gameNumber: int):
  return '''
  SELECT game_id
  FROM public."Game"
  WHERE year = '{0}' AND gameNumber = '{1}'
  '''.format(year, gameNumber)

def insertGameQuery(year_game_dict: dict):
  '''
  Insert game records into Game table.
  
  :param year_game_dict is dict of dicts, mapping years to a dict
    of game numbers, that map to the specific game information
    {
      [year]: {
        [game_num]: {}
      }
    }
  '''

  game_values = ',\n'.join([
    '''(
      {year},{game_number},'{date}',{month},'{opponent}','{result}','{home_or_away}',
      {innings},{team_wins_after},{team_losses_after},'{time}',{attendance},
      '{winning_pitcher}','{losing_pitcher}','{saving_pitcher}'
    )'''.format(year=year, **game)
    for year, game_dict in year_game_dict.items()
    for _, game in game_dict.items()
  ])

  return '''
  INSERT INTO public."Game" (
    year,
    game_number,
    date,
    month,
    opponent,
    result,
    home_or_away,
    innings,
    team_wins_after,
    team_losses_after,
    time,
    attendance,
    winning_pitcher,
    losing_pitcher,
    saving_pitcher
  ) VALUES {game_values}
  ON CONFLICT (year, game_number, date) DO NOTHING;'''.format(game_values=game_values)
  