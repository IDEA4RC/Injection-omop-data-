# Python Script to Export Data from a PostgreSQL Database to CSV Files

This Python script utilizes the psycopg2, pandas, dotenv, and os libraries to connect to a PostgreSQL database, execute SQL queries on specific tables, and export the results to CSV files. The script also loads the database credentials from a .env file to maintain information security.

### Requirements
Python 3.x
PostgreSQL
Python libraries: psycopg2, pandas, python-dotenv


### Installation
1. Clone this repository or download the export_data.py script.
2. Install dependencies by running pip install psycopg2 pandas python-dotenv.

### Usage

1. Ensure you have a .env file in the same directory as the script, with the following variables:
makefile
Copy code

```
DB_NAME=database_name
DB_USER=username
DB_PASSWORD=password
DB_HOST=host
DB_PORT=port
```

2. Run the script with python export_data.py.
3. The script will connect to the PostgreSQL database using the provided credentials, execute SQL queries on a specified list of tables, and export the results to CSV files in the same directory.

### Customization
You can modify the tables list to include or exclude specific tables from your database.
Ensure you have the necessary permissions to access the database and execute queries.

### Notes
This script is compatible with Windows, Linux, and macOS operating systems.
Ensure that the PostgreSQL user has the appropriate permissions to read the specified tables.
Note that this script will export all data from the tables to CSV files in the same directory as the script.
This README provides an overview of the script, installation requirements, usage instructions, customization options, and some important notes. You can adjust it according to your needs and preferences.
