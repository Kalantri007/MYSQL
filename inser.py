import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="car"
)

mycursor = mydb.cursor()

sql = "insert into feature value(%s,%s,%s)"
val = [
    ('city','subcompact',1200000),
    ('amaze','sports', 1500000)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

