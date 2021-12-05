def getGameIdByYearAndGameNumQuery(year: int, gameNumber: int):
  return '''
  SELECT game_id
  FROM public."Game"
  WHERE year = '{0}' AND gameNumber = '{1}'
  '''.format(year, gameNumber)

def insertGameQuery(games: list):
  '''
  Insert game records into Game table.
  '''

  game_values = ',\n'.join([
    '''(
      {year},{game_number},{date},{month},'{opponent}','{home_or_away}',
      {innings},{team_wins_after},{team_losses_after},'{time}',{attendance},
      '{winning_pitcher}','{losing_pitcher}','{saving_pitcher}'
    )'''.format(**game)
    for game in games
  ])

  return '''
  INSERT INTO public."Game" (
    year,
    game_number,
    date,
    month,
    opponent,
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
  '''.format(game_values=game_values)
  