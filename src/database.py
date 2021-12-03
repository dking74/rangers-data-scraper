import psycopg2

from config import config

def connect():
  '''
  Connect to a Postgres database.

  @see https://www.postgresqltutorial.com/postgresql-python/connect/
  @return The connection to database
  '''

  conn = None
  try:
    _config = config()
    print('Connecting to the PostgreSQL database...')
    
    conn = psycopg2.connect(**_config)
    cur = conn.cursor()

    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    db_version = cur.fetchone()
    print(db_version)

    cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)

  return conn