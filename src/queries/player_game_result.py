def insertPlayerPitchGameResultQuery(playerPitchGameResult, gameId, playerId):
  '''
  Insert a PlayerPitchGameResult object into database.
  '''

  return '''
INSERT INTO public."PlayerPitchGameResult" (

) VALUES (

)
'''.format(
  game_id=gameId,
  player_id=playerId,
  **playerPitchGameResult
)
