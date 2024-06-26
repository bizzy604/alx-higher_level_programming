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
    searched_city = sys.argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    with conn.cursor() as db_cursor:
        db_cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': searched_city
        })
        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))

    conn.close()