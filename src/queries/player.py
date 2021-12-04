def getPlayerFromRoster(first_name, last_name, year):
  '''
  '''

  return '''
SELECT Roster.player_id
FROM public."Roster" Roster
INNER JOIN public."Player" Player
ON Roster.player_id = Player.player_id
WHERE Player.first_name = {0} AND Player.last_name = {1} AND Roster.year = {2}
'''.format(first_name, last_name, year)