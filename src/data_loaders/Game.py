from src.scapers.getGame import getGamesByYear
from src.queries.game import insertGameQuery
from src.database import write_query

gameYearData = getGamesByYear()
_insertGameQuery = insertGameQuery(gameYearData)
write_query(_insertGameQuery)
print('Inserted Game entries!')