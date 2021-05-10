

import mysql.connector as  mc

mydb = mc.connect(host = "localhost",
                user = "root",
                password = "password",
                database = "car")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM order_details")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)