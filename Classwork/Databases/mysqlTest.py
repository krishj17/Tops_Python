import mysql.connector as sql

conn = sql.connect(
    host = "localhost",
    user = "root",
    password = "krish7sql",
    port = 3306,
    database = "tops26nov",
)

cur = conn.cursor()
# cur.execute("create database Tops26Nov") 
create = """
    create table student (
        stdId int primary key auto_increment,
        stdName varchar(20),
        stdAge varchar(20)
    )    
"""


# cur.executemany("insert into student values(%s,%s,%s)",[
#     (0,"krish",23),
#     (0,"yash",23),
#     (0,"mahir",23), 
#     (0,"mantan",45),
#     (0,"pranay",24),
# ])

cur.execute("update student set stdName='monton' where stdId=4")
conn.commit()