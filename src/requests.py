from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession

defaultSession = FuturesSession(max_workers=10)

def getAllData(dataDict, max_workers=10):
  '''
  Get data for a dictionary of entries.

  @param dataDict A dictionary of key id to request url.
  '''

  requests = []
  with FuturesSession(max_workers=max_workers) as session:
    for key, url in dataDict.items():
      request = session.get(url)
      request.key = key
      requests.append(request)

  results = {}
  for request in as_completed(requests):
    content = request.result().content
    results[request.key] = content

  return results

def getData(url, headers = {}):
  return defaultSession.get(url, headers=headers).result().content

def getHtmlData(url):
  return getData(url, headers={
    'Content-Type': 'text/html; charset=UTF-8',
  })