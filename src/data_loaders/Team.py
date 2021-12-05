from src.scapers.getTeam import getCoachesByYear, getManagementByYear
from src.queries.team import insertTeamCoachQuery, insertTeamManagementQuery
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