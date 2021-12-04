from bs4 import BeautifulSoup

from src.requests import getHtmlData, getAllData

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