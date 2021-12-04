from player_year_result import *

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
'{player_first_name}',
'{player_last_name}',
'{player_logo}',
{player_age},
{player_dob},
'{player_country}',
'{player_position}',
'{player_bats}',
'{player_throws}',
{player_height},
{player_weight},
{player_years}
) 
RETURNING player_id
'''.format(**player)

def insertRosterQuery(roster, playerId):
  '''
  Insert a roster object into the database.
  '''

  return '''
INSERT INTO public."Roster" (year, player_id) 
VALUES ({year}, {playerId})
'''.format(
  playerId=playerId,
  **roster
)

def insertPlayerAndData(
    player,                # Player
    roster,                # Roster
    playerBatYearResult,   # PlayerBatYearResult
    playerPitchYearResult, # PlayerPitchYearResult
    playerFieldYearResult, # PlayerFieldYearResult
):
  '''
  Insert a player, and all necessary data dependent, to the database.
  '''

  player_id = '(select player_id from player)'

  return '''
with player as (
  {player_query}
)
{roster_query}
{player_bat_year_result_query}
{player_pitch_year_result_query}
{player_field_year_result_query}
'''.format(
  player_query=insertPlayerQuery(player),
  roster_query=insertRosterQuery(roster, player_id),
  player_bat_year_result_query=insertPlayerBatYearResultQuery(playerBatYearResult, player_id),
  player_pitch_year_result_query=insertPlayerPitchYearResultQuery(playerPitchYearResult, player_id),
  player_field_year_result_query=insertPlayerFieldYearResultQuery(playerFieldYearResult, player_id),
)