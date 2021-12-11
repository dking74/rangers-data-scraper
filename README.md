# rangers-data-scraper
## Introduction
This project allows for the successful scraping of a website and inserting the data into a Postgres database.

## Setup
- To setup the database before running the scraper, type the following:
```sh
psql -U {user} -p {port} -d {database} -f ./data/ddl.sql
```
  - {user} is the username of the database; {port} is the port the database is listening on; {database} is the database to insert into.
  - This requires the 'psql' cli utility to be installed first.
  - You can also go into your Postgres instance and copy the necessary sql into an executable query window and run it.

- To run the scraper locally, you need to add database credentials. The database credentials should be stored in the [Database Config File](./config/database.ini). If the file is not present you will need to create it, and have it have the following entries:
```sh
[postgres]
host=
database=
user=
password=
```

- To install packages necessary for the virtual environment, type: `pipenv install --dev`. This requires `pipenv` to be installed. If not installed, type: `pip install pipenv` or `python -m pip install pipenv`.

## Database
The UML diagram for database construction is located at [Database Design](./docs/database_design.png). To be able to replicate the database design in PostgresSQL, run the [DDL Script](./data/ddl.sql).

## Usage
There are several different commands that can be run to load data into the database:
- `pipenv run loadAll`
  - Loads all data
- `pipenv run loadRoster`
  - Loads all roster data
- `pipenv run loadTeam`
  - Loads all team data
- `pipenv run loadGame`
  - Loads all game data
- `pipenv run loadTeamData`
  - Loads all team result data
- `pipenv run loadGameResult`
  - Loads all game result data
  - This command is in beta. It won't actually do anything

Additionally, there are two sql scripts the can be run within Postgres console or psql utility. The two scripts are:
- `./data/delete_data.sql`: Deletes all current data in the database to restart new.
- `./data/remove_database.sql`: Deletes the database to start fresh