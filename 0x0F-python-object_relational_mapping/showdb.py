#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # Connect to MySQL server
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        port=3306)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL command to show databases
    cursor.execute("SHOW DATABASES")

    # Fetch all rows from the result set
    databases = cursor.fetchall()

    # Display the databases
    for database in databases:
        print(database[0])

