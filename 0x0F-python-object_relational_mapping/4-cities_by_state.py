#!/usr/bin/python3
'''
Module: 4. Cities by states
lists all cities from the database hbtn_0e_4_usa
'''

import MySQLdb
from sys import argv


if __name__ == "__main__":

    host = 'localhost'
    port = 3306
    userName = argv[1]
    pw = argv[2]
    dbName = argv[3]

    conn = MySQLdb.connect(host=host, port=port, user=userName, passwd=pw,
                           db=dbName)
    cursor = conn.cursor()
    qry = """
    SELECT cities.id, cities.name, states.name
    FROM states
    INNER JOIN cities ON states.id = cities.state_id
    ORDER BY cities.id ASC
    """
    cursor.execute(qry)
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    conn.close()
