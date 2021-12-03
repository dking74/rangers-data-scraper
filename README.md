# rangers-data-scraper
## Introduction
This project allows for the successful scraping of a website and inserting the data into a database.

## Setup
You need to have the database credentials to run the scraper locally. The database credentials should be stored in the [Database Config File](./config/database.ini). If the file is not present you will need to create it, and have it have the following entries:
```sh
host=
database=
user=
password=
```

## Database
The UML diagram for database construction is located at [Database Design](./docs/database_design.png). To be able to replicate the database design in PostgresSQL, run the [DDL Script](./data/ddl.sql).