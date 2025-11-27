import sqlite3

conn = sqlite3.connect("testdb.db")
qry = """
    create table student (
        id int,
        name varchar(20),
        email varchar(20)
    )
"""
conn.execute(qry)
conn.commit()
conn.close()