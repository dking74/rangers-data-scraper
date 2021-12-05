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

def insertTeamResultWithPostseason(
    year: int,
    team_result_dict: dict,
    postseason_result_list: list,
):
  postseason_result_values = ',\n'.join([
    '''(team_result_id,'{series_name}','{opponent}','{result}')'''.format(**result)
    for result in postseason_result_list
  ])

  return '''WITH team_result_id as (
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
      RETURNING team_result_id
  )
  INSERT INTO public."TeamPostseasonResult" (
    team_result_id,
    series_name,
    opponent,
    resultpostseason_result_valu
  )
  VALUES {postseason_result_values}
  ON CONFLICT (year, series_name) DO NOTHING;'''.format(
    year=year,
    wins=team_result_dict.wins,
    losses=team_result_dict.losses,
    ties=team_result_dict.ties,
    division_place=team_result_dict.division_place,
    attendance=team_result_dict.attendance,
    postseason_result_values=postseason_result_values
  )