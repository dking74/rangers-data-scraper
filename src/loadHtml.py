from bs4 import BeautifulSoup

from src.requests import getHtmlData, getAllData
from src.variables import years, team_roster_url

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

# Global to not have to load html page more than once
# and return the cached version while in same script run.
team_roster_data_html = None
def loadTeamRosterHtml():
  '''Load html for the home page of team for all years'''

  global team_roster_data_html

  if team_roster_data_html is not None:
    return team_roster_data_html

  year_dict = {}
  for year in years:
    year_dict[year] = team_roster_url.format(year=year)
  team_roster_data_html = loadAllHtml(year_dict)
  return team_roster_data_html