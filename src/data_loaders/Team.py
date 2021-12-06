from src.scapers.getTeam import getCoachesByYear, getManagementByYear, getTeamResultByYear
from src.queries.team import insertTeamCoachQuery, insertTeamManagementQuery
from src.queries.team_year_result import insertAllTeamResultQuery
from src.database import write_query

# Insert TeamCoach entries
coachesByYear = getCoachesByYear()
insertCoachesQuery = insertTeamCoachQuery(coachesByYear)
write_query(insertCoachesQuery)
print('Inserted TeamCoach entries!')

# Insert TeamManagement entries
teamManagementByYear = getManagementByYear()
insertManagementQuery = insertTeamManagementQuery(teamManagementByYear)
write_query(insertManagementQuery)
print('Inserted TeamManagement entries!')

# Insert TeamResult/TeamPostseasonResult entries
teamResultByYear = getTeamResultByYear()
insertTeamResultQuery = insertAllTeamResultQuery(teamResultByYear)
write_query(insertTeamResultQuery)
print('Inserted TeamResult/TeamPostseasonResult entries!')