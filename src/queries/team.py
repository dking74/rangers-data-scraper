def insertTeamManagementQuery(
  year_management_dict: dict
) -> str:
  '''
  Insert all records into TeamManagement table.
  '''

  year_team_managements_values = ',\n'.join([
    '''({year},'{manager}','{general_manager}','{president}')'''.format(
      year=year,
      manager=team_management.manager,
      general_manager=team_management.general_manager,
      president=team_management.president
    )
    for year, team_management in year_management_dict
  ])

  return '''
INSERT INTO public."TeamManagement" (
  year,
  manager,
  general_manager,
  president
) VALUES {team_managements}
'''.format(team_managements=year_team_managements_values)

def insertTeamCoachQuery(
  year_coach_dict: dict
) -> str:
  '''
  Insert all records into TeamCoach table.
  '''

  year_team_coach_values = ',\n'.join([
    '''({year},'{name}','{coach_type}')'''.format(
      year=year,
      name=team_coach.name,
      coach_type=team_coach.coach_type
    )
    for year, team_coach in year_coach_dict
  ])

  return '''
INSERT INTO public."TeamManagement" (
  year,
  name,
  coach_type
) VALUES {team_coaches}
'''.format(team_coaches=year_team_coach_values)