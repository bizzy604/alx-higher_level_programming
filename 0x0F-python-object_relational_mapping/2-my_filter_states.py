#!/usr/bin/python3
"""
a script that takes in an argument
displays all values in the 'states' table of hbtn_0e_0_usa
where 'name' matches the argument.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_searched = sys.argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    curs = conn.cursor()
    curs.execute(
        "SELECT * FROM states WHERE name = '{}'".format(name_searched))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    conn.close()