def insertTeamBatYearResultsQuery(year_team_bat_stats_dict: dict):
  team_year_results = ',\n'.join([
    '''({year},{games},{plate_appearances},{at_bats},
    {runs},{hits},{doubles},{triples},{home_runs},{rbis},
    {stolen_bases},{caught_stealing},{walks},{strikeouts},
    {batting_average},{obp},{slg},{ops},{ops_plus},{total_bases},
    {gdp},{hbp},{sacrifice_fly},{ibb})'''.format(
      year=year,
      **team_bat_stats
    )
    for year, team_bat_stats in year_team_bat_stats_dict.items()
  ])

  return '''
  INSERT INTO public."TeamBatYearResult" (
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
  ) VALUES {team_year_results}
  ON CONFLICT (year) DO NOTHING;'''.format(team_year_results=team_year_results)

def insertTeamPitchYearResultsQuery(year_team_pitch_stats_dict: dict):
  team_year_results = ',\n'.join([
    '''({year},{wins},{losses},{win_percentage},{era},{games},
    {games_started},{games_finished},{complete_games},{shutouts},
    {saves},{innings_pitched},{hits},{runs},{earned_runs},{home_runs},
    {walks},{intentional_walks},{strikeouts},{hbp},{balks},{wild_pitches},
    {batters_faced},{era_plus},{fip},{whip},{hits_per_9},{bb_per_9},{k_per_9})'''
    .format(
      year=year,
      **team_pitch_stats
    )
    for year, team_pitch_stats in year_team_pitch_stats_dict.items()
  ])

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
  ) VALUES {team_year_results}
  ON CONFLICT (year) DO NOTHING;'''.format(team_year_results=team_year_results)

def insertTeamFieldYearResultsQuery(year_team_field_stats_dict: dict):
  team_year_results = ',\n'.join([
    '''({year},{games},{games_started},{innings},{putouts},
    {assists},{errors},{double_plays},{fielding_percentage},
    {drs},{drs_per_year})'''.format(
      year=year,
      **team_field_stats
    )
    for year, team_field_stats in year_team_field_stats_dict.items()
  ])

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
  ) VALUES {team_year_results}
  ON CONFLICT (year) DO NOTHING;'''.format(team_year_results=team_year_results)

def insertTeamBatYearResultQuery(teamBatYearResult: dict):
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
  )'''.format(**teamBatYearResult)

def insertTeamPitchYearResultQuery(teamPitchYearResult: dict):
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

def insertTeamFieldYearResultQuery(teamFieldYearResult: dict):
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

def insertTeamYearSplitQuery(year_team_split_dict: dict):
  '''
  Insert all records into TeamYearSplite table.
  '''

  year_team_split_values = ',\n'.join([
    '''({year},'{home_or_away}',{runs_scored},{runs_allowed})'''.format(
      year=year,
      home_or_away=team_year_split.home_or_away,
      runs_scored=team_year_split.runs_scored,
      runs_allowed=team_year_split.runs_allowed
    )
    for year, team_year_split in year_team_split_dict
  ])

  return '''
  INSERT INTO public."TeamYearSplit" (
    year,
    home_or_away,
    runs_scored,
    runs_allowed
  ) VALUES {team_year_split}
  '''.format(team_year_split=year_team_split_values)

def insertAllTeamResultQuery(team_result_year_dict: dict):
  '''
  Insert all year team results with their associated postseasons.
  '''

  return '\n'.join([
    insertTeamResultWithPostseasonQuery(year, team_result)
    for year, team_result in team_result_year_dict.items()
  ])
  
def insertTeamResultWithPostseasonQuery(year: int, team_result_dict: dict):
  postseason_result_list = team_result_dict['postseason']

  # Set the main query for inserting the team results
  insert_team_result_query = '''
  INSERT INTO public."TeamResult" (
    year,
    wins,
    losses,
    ties,
    division_place,
    attendance
  ) VALUES (
    {year},{wins},{losses},{ties},{division_place},{attendance}
  )
  ON CONFLICT (year) DO UPDATE SET year = EXCLUDED.year
  RETURNING team_result_id'''.format(
    year=year,
    wins=team_result_dict['wins'],
    losses=team_result_dict['losses'],
    ties=team_result_dict['ties'],
    division_place=team_result_dict['division_place'],
    attendance=team_result_dict['attendance'],
  )

  # Check if the postseason has entries. If so, we need to append that
  # value list and add the postseason entry in the database.
  if len(postseason_result_list) ==  0:
    return '{0};'.format(insert_team_result_query)
  
  postseason_result_values = ',\n'.join([
    '''((SELECT team_result_id FROM team_result),'{series_name}','{opponent}','{result}')'''.format(**result)
    for result in postseason_result_list
  ])

  postseason_entry = '''INSERT INTO public."TeamPostseasonResult" (
    team_result_id,
    series_name,
    opponent,
    result
  )
  VALUES {postseason_result_values}
  ON CONFLICT (team_result_id, series_name) DO NOTHING;'''.format(
    postseason_result_values=postseason_result_values
  )

  return '''WITH team_result as (
    {insert_team_result_query}
  )
  {postseason_entry}'''.format(
    insert_team_result_query=insert_team_result_query,
    postseason_entry=postseason_entry,
  )