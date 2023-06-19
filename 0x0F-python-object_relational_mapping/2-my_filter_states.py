#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
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
        db=database,
        port=3306)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Query to retrieve all states with a name starting with N
    query = "SELECT * \
            FROM states \
            WHERE CONVERT(`name` USING Latin1) \
            COLLATE Latin1_General_CS = '{}';".format(sys.argv[4])
    cursor.execute(query)

    # Fetch all rows from the result set
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)
