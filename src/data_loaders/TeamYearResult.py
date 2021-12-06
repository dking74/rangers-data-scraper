from src.scapers.getTeamData import getTeamAndPlayerBatDataByYear
from src.queries.team_year_result import insertTeamBatYearResultsQuery
from src.queries.player_year_result import insertPlayersBatYearResultQuery
from src.database import write_query

teamAndPlayerBatData = getTeamAndPlayerBatDataByYear()

# Separate out player and team years batting data so that
# separate queries can be formed as they are not dependent on another.
teamYearData = {}
playerYearData = {}
for year, player_team_data in teamAndPlayerBatData.items():
  playerYearData[year] = player_team_data['players']
  teamYearData[year] = player_team_data['team']

# Insert player year stats
playerBatResultQuery = insertPlayersBatYearResultQuery(playerYearData)
write_query(playerBatResultQuery)
print('Inserted PlayerBatYearResult entries!')

# Insert team year stats
teamBatResultQuery = insertTeamBatYearResultsQuery(teamYearData)
write_query(teamBatResultQuery)
print('Inserted TeamBatYearResult entries!')
