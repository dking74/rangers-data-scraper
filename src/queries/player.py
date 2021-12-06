def getPlayerFromRoster(first_name, last_name, year):
  '''
  Get a specific player from the roster by player first name, last name, and year.
  '''

  return '''
  SELECT Roster.player_id
  FROM public."Roster" Roster
  INNER JOIN public."Player" Player
  ON Roster.player_id = Player.player_id
  WHERE Player.first_name = '{0}' AND Player.last_name = '{1}' AND Roster.year = {2}
  '''.format(first_name, last_name, year)

def insertPlayersQuery(players):
  '''
  Insert a players object into database.
  '''

  values = ',\n'.join(['''(
    '{first_name}','{last_name}','{logo}',{age},'{dob}','{country}',
    '{position}','{bats}','{throws}','{height}',{weight},{years}
  )'''.format(**player) for player in players])

  return '''
  INSERT INTO public."Player" (
    first_name,
    last_name,
    logo,
    age,
    dob,
    country,
    position,
    bats,
    throws,
    height,
    weight,
    years
  ) VALUES {players_values} ON CONFLICT DO UPDATE;
  '''.format(players_values=values)

def insertPlayerQuery(player):
  '''
  Insert a player object into database.
  '''

  return '''
  INSERT INTO public."Player" (
    first_name,
    last_name,
    logo,
    age,
    dob,
    country,
    position,
    bats,
    throws,
    height,
    weight,
    years
  ) VALUES (
    '{first_name}',
    '{last_name}',
    '{logo}',
    {age},
    '{dob}',
    '{country}',
    '{position}',
    '{bats}',
    '{throws}',
    '{height}',
    {weight},
    {years}
  ) 
  RETURNING player_id;
  '''.format(
    logo='',
    position='',
    **player
  )

def insertRosterQuery(roster, playerId):
  '''
  Insert a roster object into the database.
  '''

  return '''
  INSERT INTO public."Roster" (year, player_id) 
  VALUES ({year}, {playerId});
  '''.format(
    playerId=playerId,
    **roster
  )

def insertRosterWithPlayersQuery(year: int, players: list):
  '''Insert roster from a list of players'''

  player_values = ',\n'.join([
    '''(
      '{first_name}','{last_name}','{logo}',{age},'{dob}','{country}',
      '{position}','{bats}','{throws}','{height}',{weight},{years}
    )'''.format(**player) for player in players
  ])

  return '''WITH player_ids as (
    INSERT INTO public."Player" (
      first_name,last_name,logo,age,dob,country,position,bats,
      throws,height,weight,years
    ) VALUES
      {player_values}
    ON CONFLICT (first_name, last_name, dob) DO UPDATE set
      first_name = EXCLUDED.first_name,
      last_name = EXCLUDED.last_name,
      dob = EXCLUDED.dob
    RETURNING player_id
  )
  INSERT INTO public."Roster" (
    year,
    player_id
  )
  SELECT {year}, player_id
  FROM player_ids
  ON CONFLICT (year, player_id) DO NOTHING;'''.format(year=year, player_values=player_values)

def insertMultipleYearsRosterQuery(playersByYearDict: dict):
  return '\n\n'.join([
    insertRosterWithPlayersQuery(year, players.values())
    for year, players in playersByYearDict.items()
  ])