#!/usr/bin/python3
"""
Module that retrieves states searched by the user
"""
import sys
import MySQLdb


def connectToDB():
    # Connecting to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    # Getting the state
    statement = "SELECT * FROM states WHERE name = '{}'".format(sys.argv[4])
    cur.execute(statement)
    rows = cur.fetchall()
    for item in rows:
        print(item)


if __name__ == "__main__":
    connectToDB()
