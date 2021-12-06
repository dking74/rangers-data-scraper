from src.scapers.getTeamData import (
  getTeamAndPlayerBatDataByYear,
  getTeamAndPlayerPitchDataByYear,
  getTeamAndPlayerFieldDataByYear
)
from src.queries.team_year_result import insertTeamBatYearResultsQuery, insertTeamPitchYearResultsQuery
from src.queries.player_year_result import insertPlayersBatYearResultQuery, insertPlayersPitchYearResultQuery
from src.database import write_query

print(
  '\n\n#########################################\n'
  '# Inserting TeamYearResult data\n'
  '#########################################'
)

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

# Insert player pitch year stats
playerPitchResultQuery = insertPlayersPitchYearResultQuery(playerPitchYearData)
write_query(playerPitchResultQuery)
print('Inserted PlayerPitchYearResult entries!')

# Insert team pitch year stats
teamPitchResultQuery = insertTeamPitchYearResultsQuery(teamPitchYearData)
write_query(teamPitchResultQuery)
print('Inserted TeamPitchYearResult entries!')

#########################################################################
# Team Fielding data is Failing because Baseball-Reference pulls this
# data via Javascript. The current implementation does not wait for JS to
# load, which is why the appropriate HTML doesn't load.
# 
# teamAndPlayerFieldData = getTeamAndPlayerFieldDataByYear()
#########################################################################


# Separate out player and team years fielding data so that
# separate queries can be formed as they are not dependent on another.
# teamPitchYearData = {}
# playerPitchYearData = {}
# for year, player_team_data in teamAndPlayerPitchData.items():
#   playerPitchYearData[year] = player_team_data['players']
#   teamPitchYearData[year] = player_team_data['team']

# # # Insert player field year stats
# playerPitchResultQuery = insertPlayersPitchYearResultQuery(playerPitchYearData)
# write_query(playerPitchResultQuery)
# print('Inserted PlayerFieldYearResult entries!')

# # Insert team field year stats
# teamPitchResultQuery = insertTeamPitchYearResultsQuery(teamPitchYearData)
# write_query(teamPitchResultQuery)
# print('Inserted TeamFieldYearResult entries!')
