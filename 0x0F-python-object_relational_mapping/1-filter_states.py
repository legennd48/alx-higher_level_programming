#!/usr/bin/python3
'''
Module: 1. Filter states
script that lists all states with a name starting with N (upper N)
'''
import MySQLdb
import sys


if __name__ == "__main__":

    userName = sys.argv[1]
    pw = sys.argv[2]
    dbName = sys.argv[3]
    host = 'localhost'
    port = 3306

    # connection to db
    conn = MySQLdb.connect(host=host, port=port, user=userName,
                           passwd=pw, db=dbName)
    # creating cursor
    cursor = conn.cursor()
    # query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    # execute query
    cursor.execute(query)

    # get results
    results = cursor.fetchall()

    # print results
    for row in results:
        print(row)

    # close cursor and connection
    cursor.close()
    conn.close()
