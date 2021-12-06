from src.queries.player import getPlayerFromRoster

def insertPlayersBatYearResultQuery(year_player_bat_stats_dict: dict):
  '''
  Insert all players-stats by year into database
  '''
  player_year_results = ',\n'.join([
    '''(({player_roster_query}),
    {year},{games},{plate_appearances},{at_bats},
    {runs},{hits},{doubles},{triples},{home_runs},{rbis},
    {stolen_bases},{caught_stealing},{walks},{strikeouts},
    {batting_average},{obp},{slg},{ops},{ops_plus},{total_bases},
    {gdp},{hbp},{sacrifice_fly},{ibb})'''.format(
      player_roster_query=getPlayerFromRoster(
        player_name.split(' ')[0],
        player_name.split(' ')[1],
        year
      ),
      year=year,
      **player_bat_stats
    )
    for year, player_bat_dict in year_player_bat_stats_dict.items()
    for player_name, player_bat_stats in player_bat_dict.items()
  ])

  return '''
  INSERT INTO public."PlayerBatYearResult" (
    player_id,
    year,
    games,
    plate_appearances,
    at_bats,
    runs,
    hits,
    doubles,
    triples,
    home_runs,
    rbis,
    stolen_bases,
    caught_stealing,
    walks,
    strikeouts,
    batting_average,
    obp,
    slg,
    ops,
    ops_plus,
    total_bases,
    gdp,
    hbp,
    sacrifice_fly,
    ibb
  ) VALUES {player_year_results}
  ON CONFLICT (year, player_id) DO NOTHING;'''.format(player_year_results=player_year_results)

def insertPlayerBatYearResultQuery(playerBatYearResult, playerId):
  '''
  Insert a PlayerBatYearResult object into database.
  '''

  return '''
INSERT INTO public."PlayerBatYearResult" (
  year,
  player_id,
  games,
  plate_appearances,
  at_bats,
  runs,
  hits,
  doubles,
  tripes,
  home_runs,
  rbis,
  stolen_bases,
  caught_stealing,
  walks,
  strikeouts,
  batting_average,
  obp,
  slg,
  ops,
  ops_plus,
  total_bases,
  gdp,
  hbp,
  sacrifice_fly,
  ibb
) VALUES (
  {year},
  {player_id},
  {games},
  {plate_appearances},
  {at_bats},
  {runs},
  {hits},
  {doubles},
  {triples},
  {home_runs},
  {rbis},
  {stolen_bases},
  {caught_stealing},
  {walks},
  {strikeouts},
  {batting_average},
  {obp},
  {slg},
  {ops},
  {ops_plus},
  {total_bases},
  {gdp},
  {hbp},
  {sacrifice_fly},
  {ibb}
)
'''.format(
  player_id=playerId
  **playerBatYearResult
)

def insertPlayerPitchYearResultQuery(playerPitchYearResult, playerId):
  '''
  Insert a PlayerPitchYearResult object into database.
  '''

  return '''
INSERT INTO public."PlayerPitchYearResult" (
  year,
  player_id,
  wins,
  losses,
  win_percentage,
  era,
  games,
  games_started,
  games_finished,
  complete_games,
  shutouts,
  saves,
  innings_pitched,
  hits,
  runs,
  earned_runs,
  home_runs,
  walks,
  intentional_walks,
  strikeouts,
  hbp,
  balks,
  wild_pitches,
  batters_faced,
  era_plus,
  fip,
  whip,
  hits_per_9,
  bb_per_9,
  k_per_9
) VALUES (
  {year},
  {player_id},
  {wins},
  {losses},
  {win_percentage},
  {era},
  {games},
  {games_started},
  {games_finished},
  {complete_games},
  {shutouts},
  {saves},
  {innings_pitched},
  {hits},
  {runs},
  {earned_runs},
  {home_runs},
  {walks},
  {intentional_walks},
  {strikeouts},
  {hbp},
  {balks},
  {wild_pitches},
  {batters_faced},
  {era_plus},
  {fip},
  {whip},
  {hits_per_9},
  {bb_per_9},
  {k_per_9}
)
'''.format(
  player_id=playerId,
  **playerPitchYearResult
)

def insertPlayerFieldYearResultQuery(playerFieldYearResult, playerId):
  '''
  Insert a PlayerFieldYearResult object into database.
  '''

  return '''
INSERT INTO public."PlayerFieldYearResult" (
  year,
  player_id,
  games,
  games_started,
  innings,
  putouts,
  assists,
  errors,
  double_plays,
  fielding_percentage,
  drs,
  drs_per_year
) VALUES (
  {year},
  {player_id},
  {games},
  {games_started},
  {innings},
  {putouts},
  {assists},
  {errors},
  {double_plays},
  {fielding_percentage},
  {drs},
  {drs_per_year}
)
'''.format(
  player_id=playerId,
  **playerFieldYearResult
)