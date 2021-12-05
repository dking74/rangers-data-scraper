import re
from src.loadHtml import loadTeamRosterHtml

def setCoachDefaults(name):
  return {
    'name': name,
    'coach_type': ''
  }

def getCoachesByYear(year_team_roster_data: dict = None) -> dict:
  '''
  Find coaches in html for each year.
  '''

  if year_team_roster_data is None:
    year_team_roster_data = loadTeamRosterHtml()

  # Go through each entry of soup content loaded from remote resource
  # and create a Coach entry found from within html
  coaches_year_data = {}
  for year, soup in year_team_roster_data.items():
    coaches_data = {}
    coach_rows = soup.select('#all_coaches #div_coaches #coaches tbody tr')
    for coach_row in coach_rows:
      coach_name_header = coach_row.select_one('th')
      coach_name_link = coach_name_header.select_one('a')
      coach_name: str = coach_name_link.text if coach_name_link is not None else coach_name_header.text

      # Create a new player entry for storage and assign name
      # if the entry has not already been created.
      if coach_name not in coaches_data:
        coaches_data[coach_name] = setCoachDefaults(coach_name)

      coach_data = coach_row.select('td')
      for data_td in coach_data:
        data_stat = data_td.attrs['data-stat']
        if data_stat == 'coach_type':
          coaches_data[coach_name]['coach_type'] = data_td.text
      coaches_year_data[year] = coaches_data.values()

  return coaches_year_data

def __getParagraphTeamInfo(paragraph_info_section):
  link = paragraph_info_section.find('a')
  return re.match(
    r"[A-Za-z\s ]+",
    link.text if link is not None else paragraph_info_section.contents[2]
  ).group(0).strip()

def getManagementByYear(year_team_roster_data: dict = None) -> dict:
  '''
  Find team management in html for each year.
  '''

  if year_team_roster_data is None:
    year_team_roster_data = loadTeamRosterHtml()

  team_management_year_data = {}
  for year, soup in year_team_roster_data.items():
    team_management_year_data[year] = {
      'manager': '',
      'president': '',
      'general_manager': ''
    }
    soup = year_team_roster_data[year]
    team_info_section = soup.select('#info #meta div[data-template="Partials/Teams/Summary"] p')
    for section in team_info_section:
      header = section.find('strong').text.strip()
      if header == 'Manager:' or header == 'Managers:':
        team_management_year_data[year]['manager'] = __getParagraphTeamInfo(section)
      if header == 'President:':
        team_management_year_data[year]['president'] = __getParagraphTeamInfo(section)
      if header == 'General Manager:':
        team_management_year_data[year]['general_manager'] = __getParagraphTeamInfo(section)

  return team_management_year_data