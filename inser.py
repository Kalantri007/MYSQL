import mysql.connector

class DB:

    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",
                                            user="root",
                                            password="password",
                                            database="car")
        c = self.mydb.cursor()

    def insert_CD(self,SR,model,stock,launch_date,car_description):
        que = "INSERT INTO car_details VALUES ({},'{}',{},'{}','{}')".format(SR,model,stock,launch_date,car_description)
        print(que)
        c = self.mydb.cursor()
        c.execute(que)
        self.mydb.commit()
        print("done insert_CD")

    def insert_FT(self,model, car_type, price):
        que = "INSERT INTO feature VALUES ('{}','{}','{}')".format(model, car_type, price)
        print(que)
        c = self.mydb.cursor()
        c.execute(que)
        self.mydb.commit()
        print("done inser_FT")

    def print_CD(self):
        que = "SELECT * FROM car_details"
        c = self.mydb.cursor()
        c.execute(que)
        for row in c:
            print(row)

    def print_FT(self):
        que = "SELECT * FROM feature"
        c = self.mydb.cursor()
        c.execute(que)
        for row in c:
            print(row)

    def del_CD(self, id):
        que = "DELETE FROM car_details WHERE SR= {}".format(id)
        print(que)
        c = self.mydb.cursor()
        c.execute(que)
        self.mydb.commit()
        print("CD data DELETED")

    def del_FT(self, model):
        que = "DELETE FROM feature WHERE model= '{}'".format(model)
        print(que)
        c = self.mydb.cursor()
        c.execute(que)
        self.mydb.commit()
        print("FT data DELETED")

obj = DB()

obj.insert_FT('city','compact car','1200000')
obj.insert_FT('amaze','sports car','1500000')
obj.insert_CD(1,'city', 10, '2021-05-01', 'nice cat')
obj.insert_CD(2,'amaze', 15, '2021-05-02','good cat')
# obj.print_CD()
# obj.print_FT()
# obj.del_FT('city')
# obj.del_FT('amaze')
# obj.print_FT()

# obj.del_CD(1)
# obj.del_CD(2)
# obj.print_CD()

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

