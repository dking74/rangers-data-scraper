from src.scapers.getRoster import getPlayersByYear
from src.queries.player import insertMultipleYearsRosterQuery
from src.database import write_query, fetch_all_query

playersByYear = getPlayersByYear()
insertRosterQuery = insertMultipleYearsRosterQuery(playersByYear)
write_query(insertRosterQuery)