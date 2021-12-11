from src.loadHtml import loadTeamRosterHtml
from src.utility.string_utils import (
  getParagraphTeamInfo,
  matchStandardString,
  getOneMatch,
  compilePattern,
  replace_single_quote,
)
from src.utility.types_utils import setCoachDefaults

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
    coaches_data = []
    coach_rows = soup.select('#all_coaches #div_coaches #coaches tbody tr')
    for coach_row in coach_rows:
      coach_name_header = coach_row.select_one('th')
      coach_name_link = coach_name_header.select_one('a')
      coach_name: str = coach_name_link.text if coach_name_link is not None else coach_name_header.text
      coach_name = replace_single_quote(coach_name)

      # Set initial, default coach data
      coach_data = setCoachDefaults(coach_name)

      coach_td_data = coach_row.select('td')
      for data_td in coach_td_data:
        data_stat = data_td.attrs['data-stat']
        if data_stat == 'coach_type':
          coach_data['coach_type'] = data_td.text
      if coach_data['coach_type'] != 'Manager':
        coaches_data.append(coach_data)
    coaches_year_data[year] = coaches_data

  return coaches_year_data

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
    # soup = year_team_roster_data[year]
    team_info_section = soup.select('#info #meta div[data-template="Partials/Teams/Summary"] p')
    for section in team_info_section:
      header = section.find('strong').text.strip()
      if header == 'Manager:' or header == 'Managers:':
        team_management_year_data[year]['manager'] = getParagraphTeamInfo(section)
      if header == 'President:':
        team_management_year_data[year]['president'] = getParagraphTeamInfo(section)
      if header == 'General Manager:':
        team_management_year_data[year]['general_manager'] = getParagraphTeamInfo(section)

  return team_management_year_data

def getTeamResultByYear(year_team_roster_data: dict = None) -> dict:
  '''
  Find team result in html for each year.
  '''

  if year_team_roster_data is None:
    year_team_roster_data = loadTeamRosterHtml()

  team_result_year_data = {}
  for year, soup in year_team_roster_data.items():
    team_result_year_data[year] = {
      'wins': 0,
      'losses': 0,
      'ties': 0,
      'division_place': 1,
      'attendance': 0,
      'postseason': []
    }
    team_info_section = soup.select('#info #meta div[data-template="Partials/Teams/Summary"] p')
    for section in team_info_section:
      header = section.find('strong')
      header_text = header.text.strip()
      header_contents = section.contents[2]
      if header_text == 'Record:':
        record_place_entry = header_contents.split(',')

        # Parse the record field into wins/losses/ties
        record = matchStandardString(record_place_entry[0]).split('-')
        team_result_year_data[year]['wins'] = int(record[0])
        team_result_year_data[year]['losses'] = int(record[1])
        team_result_year_data[year]['ties'] = int(record[2])
        
        # Parse the divison finishing field and get place of team
        place_record = matchStandardString(record_place_entry[1])
        place = getOneMatch(r"\d", place_record)
        team_result_year_data[year]['division_place'] = int(place)
      if header_text == 'Postseason:':
        # Get the series result (win or lost)
        series_results_unfiltered = section.find_all(string=compilePattern('Lost|Won'))
        series_results = [
          'win' if series_result.strip() == 'Lost' else 'loss'
          for series_result in series_results_unfiltered
        ]

        # Get the series titles
        series_type_tags = section.find_all('a', title=False)
        series_types = [getOneMatch(r"[A-Za-z ]+", series_type.text) for series_type in series_type_tags]

        # Get the series opponents
        series_opponents_tags = section.find_all('a', title=True)
        series_opponents = [opponent_tag.text for opponent_tag in series_opponents_tags]

        postseason_results = []
        for i in range(len(series_results)):
          postseason_results.append({
            'series_name': '' if len(series_types) < i + 1 else series_types[i],
            'opponent': '' if len(series_opponents) < i + 1 else series_opponents[i],
            'result': '' if len(series_results) < i + 1 else series_results[i],
          })
        team_result_year_data[year]['postseason'] = postseason_results
      if header_text == 'Attendance:':
        attendance = getOneMatch(r"[\d,]+", header_contents)
        team_result_year_data[year]['attendance'] = int(attendance.replace(",", ""))

  return team_result_year_data