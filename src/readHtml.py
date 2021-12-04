from requests import get
from bs4 import BeautifulSoup

def readHtml(siteUrl) -> str:
  return get(siteUrl, headers={
    'Content-Type': 'text/html; charset=UTF-8',
  }).content

def loadHtml(htmlUrl):
  html = readHtml(htmlUrl)
  return BeautifulSoup(html, features="html.parser")