#!/usr/bin/python3
"""
A script that drops a specified database in MySQL
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db="mysql",
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Drop the specified database
    drop_query = "DROP DATABASE {}".format(database)
    cursor.execute(drop_query)

    print("Database {} has been dropped.".format(database))

    # Close the cursor and database connection
    cursor.close()
    db.close()

