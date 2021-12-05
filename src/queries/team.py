def insertTeamManagementQuery(
  year_management_dict: dict
) -> str:
  '''
  Insert all records into TeamManagement table.
  '''

  year_team_managements_values = ',\n'.join([
    '''({year},'{manager}','{general_manager}','{president}')'''.format(
      year=year,
      manager=team_management['manager'],
      general_manager=team_management['general_manager'],
      president=team_management['president']
    )
    for year, team_management in year_management_dict.items()
  ])

  return '''
  INSERT INTO public."TeamManagement" (
    year,
    manager,
    general_manager,
    president
  ) VALUES {team_managements}
  ON CONFLICT (year, manager, general_manager, president) DO UPDATE SET
    year = EXCLUDED.year,
    manager = EXCLUDED.manager,
    general_manager = EXCLUDED.general_manager,
    president = EXCLUDED.president
  '''.format(team_managements=year_team_managements_values)

def insertTeamCoachQuery(
  year_coach_dict: dict
) -> str:
  '''
  Insert all records into TeamCoach table.
  '''

  coach_entries = []
  for year, team_coach_year_array in year_coach_dict.items():
    for team_coach in team_coach_year_array:
      coach_entry = '''({year},'{name}','{coach_type}')'''.format(
        year=year,
        name=team_coach['name'],
        coach_type=team_coach['coach_type']
      )
      coach_entries.append(coach_entry)
  year_team_coach_values = ',\n'.join(coach_entries)

  return '''
  INSERT INTO public."TeamCoach" (
    year,
    name,
    coach_type
  ) VALUES {team_coaches}
  ON CONFLICT (year, name) DO UPDATE SET
    year = EXCLUDED.year,
    name = EXCLUDED.name
  '''.format(team_coaches=year_team_coach_values)