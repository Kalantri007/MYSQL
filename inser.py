import mysql.connector

class DB:

    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",
                                            user="root",
                                            password="password",
                                            database="car")
        c = self.mydb.cursor()

    def insert(self,SR,model,stock,launch_date,car_description)
        que = "INSERT INTO car_details VALUES ({},'{}',{},'{}','{}')".format(SR,model,stock,launch_date,car_description)
        print(que)
        c = self.mydb.cursor()
        c.execute(que)
        self.mydb.commit()
        print("done!!!")

    def print_data(self):
        que = "SELECT * FROM car_details"
        c = self.mydb.cursor()
        c.execute(que)

        for row in c:
            print(row)

    def del_data(self, id):
        que = "DELETE FROM car_details WHERE SR= {}".format(id)
        print(que)
        c = self.mydb.cursor()
        c.execute(que)
        self.mydb.commit()
        print("DATA DELETED")




obj = DB()
obj.print_data()
obj.del_data()
obj.print_data()

# obj.insert(1,'city', 10, '2021-05-01', 'nice cat')
# obj.insert(2,'amaze', 15, '2021-05-02','good cat')

# sql = "insert into feature value(%s,%s,%s)"
# val = [
#     ('city','subcompact',1200000),
#     ('amaze','sports', 1500000)
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

