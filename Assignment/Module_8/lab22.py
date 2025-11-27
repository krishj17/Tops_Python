import sqlite3

conn = sqlite3.connect("testdb.db")

conn.executemany("insert into student values(?,?,?)",[
    (110,"alice","alice@gmail.com"),
    (111,"smith","smith@gmail.com")
])

select = "select * from student;"
data = conn.execute(select)
print(data.fetchall())


conn.commit()
conn.close()