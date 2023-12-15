#!/usr/bin/python3
'''
Module: 0. Get all states
lists all states from the database hbtn_0e_0_usa:
'''
import MySQLdb
import sys


if __name__ == "__main__":

    userName = sys.argv[1]
    pw = sys.argv[2]
    name = sys.argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306, user=userName,
                           passwd=pw, db=name)
    # create cursor for queries
    cursor = conn.cursor()
    query = 'SELECT * FROM states ORDER BY states.id ASC'

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()
