def setGameDefaults(game_number: int):
  return {
    'game_number': game_number,
    'date': '',
    'month': 1,
    'opponent': '',
    'home_or_away': 'home',
    'innings': 9,
    'result': 'W',
    'team_wins_after': 0,
    'team_losses_after': 0,
    'time': '00:00',
    'attendance': 0,
    'winning_pitcher': '',
    'losing_pitcher': '',
    'saving_pitcher': '',
  }

def setPlayerDefaults(first_name: str = '', last_name: str = ''):
  return {
    'first_name': first_name,
    'last_name': last_name,
    'age': '',
    'country': 'US',
    'bats': 'R',
    'throws': 'R',
    'height': '',
    'weight': 0,
    'dob': '',
    'years': 0,
    'logo': '',
    'position': ''
  }

def setCoachDefaults(name):
  return {
    'name': name,
    'coach_type': ''
  }

def setBattingStatsDefaults():
  return {
    'games': 0,
    'plate_appearances': 0,
    'at_bats': 0,
    'runs': 0,
    'hits': 0,
    'doubles': 0,
    'triples': 0,
    'home_runs': 0,
    'rbis': 0,
    'stolen_bases': 0,
    'caught_stealing': 0,
    'walks': 0,
    'strikeouts': 0,
    'batting_average': 0,
    'obp': 0,
    'slg': 0,
    'ops': 0,
    'ops_plus': 0,
    'total_bases': 0,
    'gdp': 0,
    'hbp': 0,
    'sacrifice_fly': 0,
    'ibb': 0
  }

def setPitchingStatsDefaults():
  return {
    'wins': 0,
    'losses': 0,
    'win_percentage': 0,
    'era': 0,
    'games': 0,
    'games_started': 0,
    'games_finished': 0,
    'complete_games': 0,
    'shutouts': 0,
    'saves': 0,
    'innings_pitched': 0,
    'hits': 0,
    'runs': 0,
    'earned_runs': 0,
    'home_runs': 0,
    'walks': 0,
    'intentional_walks': 0,
    'strikeouts': 0,
    'hbp': 0,
    'balks': 0,
    'wild_pitches': 0,
    'batters_faced': 0,
    'era_plus': 0,
    'fip': 0,
    'whip': 0,
    'hits_per_9': 0,
    'bb_per_9': 0,
    'k_per_9': 0,
  }