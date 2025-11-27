import sqlite3

conn = sqlite3.connect("testdb.db")

qry = """
    create table student (
        id int,
        name varchar(20),
        email varchar(20)
    )
"""
qry1=   "insert into student values (101,'krish','krish@gmail.com');"
qry2=    "insert into student values (102,'harsh','harsh@gmail.com');"
qry3=     "insert into student values (103,'mahir','mahir@gmail.com');"
qry4=     "insert into student values (104,'yash','yash@gmail.com');"
qry5=     "insert into student values (105,'pranay','pranay@gmail.com');"

# conn.executemany("insert into student values(?,?,?)",[
#     (110,"alice","alice@gmail.com"),
#     (111,"smith","smith@gmail.com")
# ])

update = "update student set name='pandya' where id=102"

delete = "delete from student where id=104"

# select = "select * from student;"
# data = conn.execute(select)
# for i in data.fetchall():
#     print(i)

conn.commit()