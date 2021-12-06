from src.scapers.getTeamData import getTeamAndPlayerBatDataByYear, getTeamAndPlayerPitchDataByYear
from src.queries.team_year_result import insertTeamBatYearResultsQuery, insertTeamPitchYearResultsQuery
from src.queries.player_year_result import insertPlayersBatYearResultQuery, insertPlayersPitchYearResultQuery
from src.database import write_query

teamAndPlayerBatData = getTeamAndPlayerBatDataByYear()

# Separate out player and team years batting data so that
# separate queries can be formed as they are not dependent on another.
teamBatYearData = {}
playerBatYearData = {}
for year, player_team_data in teamAndPlayerBatData.items():
  playerBatYearData[year] = player_team_data['players']
  teamBatYearData[year] = player_team_data['team']

# Insert player bat year stats
playerBatResultQuery = insertPlayersBatYearResultQuery(playerBatYearData)
write_query(playerBatResultQuery)
print('Inserted PlayerBatYearResult entries!')

# Insert team bat year stats
teamBatResultQuery = insertTeamBatYearResultsQuery(teamBatYearData)
write_query(teamBatResultQuery)
print('Inserted TeamBatYearResult entries!')


teamAndPlayerPitchData = getTeamAndPlayerPitchDataByYear()

# Separate out player and team years pitching data so that
# separate queries can be formed as they are not dependent on another.
teamPitchYearData = {}
playerPitchYearData = {}
for year, player_team_data in teamAndPlayerPitchData.items():
  playerPitchYearData[year] = player_team_data['players']
  teamPitchYearData[year] = player_team_data['team']

# # Insert player pitch year stats
playerPitchResultQuery = insertPlayersPitchYearResultQuery(playerPitchYearData)
write_query(playerPitchResultQuery)
print('Inserted PlayerPitchYearResult entries!')

# Insert team pitch year stats
teamPitchResultQuery = insertTeamPitchYearResultsQuery(teamPitchYearData)
write_query(teamPitchResultQuery)
print('Inserted TeamPitchYearResult entries!')
