def insertTeamBatYearResultQuery(teamBatYearResult):
  '''
  Insert a TeamBatYearResult object into database.
  '''

  return '''
INSERT INTO public."TeamBatYearResult" (
  year,
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
'''.format(**teamBatYearResult)

def insertTeamBatYearResultQuery(teamPitchYearResult):
  '''
  Insert a TeamPitchYearResult object into database.
  '''

  return '''
INSERT INTO public."TeamPitchYearResult" (
  year,
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
'''.format(**teamPitchYearResult)

def insertTeamFieldYearResultQuery(teamFieldYearResult):
  '''
  Insert a TeamFieldYearResult object into database.
  '''

  return '''
INSERT INTO public."TeamFieldYearResult" (
  year,
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
'''.format(**teamFieldYearResult)