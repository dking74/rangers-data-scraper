import sys
import psycopg2

from src.variables import database_config

# Global connection instance to database
conn = None

def connect():
  '''
  Connect to a Postgres database.

  @see https://www.postgresqltutorial.com/postgresql-python/connect/
  @return The connection to database
  '''

  global conn

  try:
    _config = database_config
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

    conn.close()
    sys.exit(1)

  return conn

def get_connection():
  '''
  Gets the global database connection, or if not set, establish
  the connection and then return it back.
  '''

  global conn
  return conn or connect()

def __getCursor():
  connection = get_connection()
  return connection, connection.cursor()

def write_query(query: str, vars: list = []):
  conn, cursor = __getCursor()
  try:
    cursor.execute(query, vars)
    conn.commit()
  except Exception as e:
    print("Error occurred executing query: {0}".format(e))
    cursor.close()
    return None
  return cursor

def get_query(query: str, vars: list = []):
  conn, cursor = __getCursor()
  try:
    cursor.execute(query, vars)
  except Exception as e:
    print("Error occurred executing query: {0}".format(e))
    cursor.close()
    return None

  return cursor

def fetch_all_query(query: str, vars: list = []):
  '''Query to fetch all resources from database'''
  cursor = get_query(query, vars)
  return cursor.fetchall()

def fetch_many_query(query: str, size: int, vars: list = []):
  '''Query to fetch many ('size' records) resources from database'''
  cursor = get_query(query, vars)
  return cursor.fetchmany(size=size)

def fetch_one_query(query: str, vars: list = []):
  '''Query to fetch one resource from database'''
  cursor = get_query(query, vars)
  return cursor.fetchone()