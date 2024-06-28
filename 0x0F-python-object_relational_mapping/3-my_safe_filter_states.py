#!/usr/bin/python3
"""
a script that takes in an argument
displays all values in the 'states' table of hbtn_0e_0_usa
where 'name' matches the argument.
Safe from MySQL injections.
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
    curs.execute("SELECT * FROM states;")
    rows = curs.fetchall()
    for row in rows:
        if name_searched == row[1]:
            print(row)
    curs.close()
    conn.close()