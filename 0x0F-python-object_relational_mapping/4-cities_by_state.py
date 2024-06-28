#!/usr/bin/python3
"""
lists all 'cities' from the database 'hbtn_0e_4_usa'
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    curs = conn.cursor()

    curs.execute('''
        SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON cities.state_id=states.id
        ORDER BY cities.id ASC
        ''')
    query_rows = curs.fetchall()

    for row in query_rows:
        print(row)

    curs.close()
    conn.close()