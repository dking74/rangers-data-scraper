from bs4 import BeautifulSoup

from src.requests import getHtmlData, getAllData
from src.variables import (
  years,
  team_home_url,
  team_roster_url,
  team_schedule_url,
  team_fielding_url
)

def loadAllHtml(urlMapping):
  '''
  Load html for a dict of key to url.
  The method will asynchronously load all html pages, and combine
  them into a single entity. For each entry, load the Beautiful soup
  parsed content.

  @returns A dict of key to BeautifulSoup PageElement
  '''

  data = getAllData(urlMapping)

  mapped_data = {}
  for key, html_content in data.items():
    mapped_data[key] = BeautifulSoup(html_content, features="html.parser")
  return mapped_data

def loadHtml(htmlUrl):
  '''
  Load BeautifulSoup content for a single html url.
  '''

  html = getHtmlData(htmlUrl)
  return BeautifulSoup(html, features="html.parser")

# Global to not have to load roster html page more than once
# and return the cached version while in same script run.
team_home_data_html = None
def loadTeamHomeHtml():
  '''Load html for the home page of team for all years'''

  global team_home_data_html

  if team_home_data_html is not None:
    return team_home_data_html

  year_dict = {}
  for year in years:
    year_dict[year] = team_home_url.format(year=year)
  team_home_data_html = loadAllHtml(year_dict)
  return team_home_data_html

# Global to not have to load roster html page more than once
# and return the cached version while in same script run.
team_roster_data_html = None
def loadTeamRosterHtml():
  '''Load html for the roster page of team for all years'''

  global team_roster_data_html

  if team_roster_data_html is not None:
    return team_roster_data_html

  year_dict = {}
  for year in years:
    year_dict[year] = team_roster_url.format(year=year)
  team_roster_data_html = loadAllHtml(year_dict)
  return team_roster_data_html

# Global to not have to load schedule html page more than once
# and return the cached version while in same script run.
team_schedule_data_html = None
def loadTeamScheduleHtml():
  '''Load html for the schedule page of team for all years'''

  global team_schedule_data_html

  if team_schedule_data_html is not None:
    return team_schedule_data_html

  year_dict = {}
  for year in years:
    year_dict[year] = team_schedule_url.format(year=year)
  team_schedule_data_html = loadAllHtml(year_dict)
  return team_schedule_data_html

# Global to not have to load schedule html page more than once
# and return the cached version while in same script run.
team_fielding_data_html = None
def loadTeamFieldingHtml():
  '''Load html for the fielding page of team for all years'''

  global team_fielding_data_html

  if team_fielding_data_html is not None:
    return team_fielding_data_html

  year_dict = {}
  for year in years:
    year_dict[year] = team_fielding_url.format(year=year)
  team_fielding_data_html = loadAllHtml(year_dict)
  return team_fielding_data_html