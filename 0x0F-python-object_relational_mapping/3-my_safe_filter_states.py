#!/usr/bin/python3
'''
Module:  3. SQL Injection...
recieves 4 arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the 4th argument. and
not vulnerable to SQL injections
'''

import MySQLdb
from sys import argv


if __name__ == "__main__":

    host = 'localhost'
    port = 3306
    userName = argv[1]
    pw = argv[2]
    dbName = argv[3]
    searchd = argv[4]

    conn = MySQLdb.connect(host=host, port=port, user=userName, passwd=pw,
                           db=dbName)
    cursor = conn.cursor()
    qry = """SELECT * FROM states
             WHERE name=%s
             ORDER BY states.id ASC"""
    cursor.execute(qry, (searchd,))
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    conn.close()
