#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Arguments: username, password, database name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    # Fetch all states ordered by id ASC
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    # Print rows exactly in the required format
    for row in rows:
        print(row)

    cur.close()
    db.close()

