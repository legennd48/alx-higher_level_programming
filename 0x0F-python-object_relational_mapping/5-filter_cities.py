#!/usr/bin/python3
'''
Module: 5. All cities by state
 takes in the name of a state as an argument
and lists all cities of that state
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    host = 'localhost'
    port = 3306
    userName = argv[1]
    pw = argv[2]
    dbName = argv[3]
    stateName = argv[4]

    conn = MySQLdb.connect(host=host, port=port, user=userName, passwd=pw,
                           db=dbName)
    cur = conn.cursor()
    qry = '''
    SELECT name FROM cities
    WHERE cities.state_id = (SELECT states.id FROM states
    WHERE states.name=%s)
    '''
    cur.execute(qry, (stateName,))
    result = cur.fetchall()
    print(', '.join(['{}'.format(row[0]) for row in result]))

    cur.close()
    conn.close()
