def getPlayerIdByFirstAndLast(first_name, last_name):
  '''
  Get the player id by the user first_name and last_name
  '''

  return '''
SELECT player_id
FROM public."Player"
WHERE first_name = '{0}' AND last_name = '{1}
'''.format(first_name, last_name)