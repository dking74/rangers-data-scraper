from src.scapers.getRoster import getPlayersByYear
from src.queries.player import insertMultipleYearsRosterQuery
from src.database import write_query

print(
  '\n\n#########################################\n'
  '# Inserting Roster data\n'
  '#########################################'
)

# Insert Player and Roster entries
playersByYear = getPlayersByYear()
insertRosterQuery = insertMultipleYearsRosterQuery(playersByYear)
write_query(insertRosterQuery)
print('Inserted Player/Roster entries!')