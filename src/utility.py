import re

def compilePattern(pattern):
  return re.compile(pattern)

def getOneMatch(regex_string, string) -> str:
  '''
  Use custom regex string to find the first match.
  Returns 'None' if no match is found.
  '''

  match = re.search(regex_string, string)
  return match.group(0).strip() if match is not None else None

def matchStandardString(string_entry) -> str:
  '''
  Match standard, accepted characters in paragraph fields to get rid
  of bad character entries we don't want to keep.
  '''

  return getOneMatch(r"[A-Za-z0-9\-\s ]+", string_entry)

def getParagraphTeamInfo(paragraph_info_section) -> str:
  '''
  Utility method to scrape standard paragraph section in team info
  section and simply return the necessary detail.
  '''

  link = paragraph_info_section.find('a')
  return matchStandardString(
    link.text if link is not None else paragraph_info_section.contents[2]
  )