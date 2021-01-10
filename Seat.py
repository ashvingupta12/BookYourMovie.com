import mysql.connector
class Seat:
    def show_seats(self):
        mydb = mysql.connector.connect(user='admin', password='root', host='localhost', database='BOOKMYMOVIE')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT ROW_NUM,COL_NUM,SEAT_STATUS FROM BOOKINGS")
        myresult=mycursor.fetchall()
        return myresult
    def book_seat(self,row,column):
        mydb = mysql.connector.connect(user='admin', password='root', host='localhost', database='BOOKMYMOVIE')
        mycursor = mydb.cursor()
        sql="SELECT SEAT_STATUS,PRICE FROM BOOKINGS WHERE ROW_NUM=%s AND COL_NUM=%s"
        val=(row,column)
        mycursor.execute(sql,val)
        status=mycursor.fetchall()
        return status
    def update_seat(self,row,column):
        mydb = mysql.connector.connect(user='admin', password='root', host='localhost', database='BOOKMYMOVIE')
        mycursor = mydb.cursor()
        user=input("Enter your name:")
        gender = input("Enter your gender(M/F):")
        Age = input("Enter your age:")
        phone_no = input("Enter your phone_no:")
        sql_u="INSERT INTO USER VALUES (%s,%s,%s,%s)"
        val_u=(user,gender,Age,phone_no)
        mycursor.execute(sql_u,val_u)
        sql = "UPDATE BOOKINGS SET SEAT_STATUS='B',USER=%s WHERE ROW_NUM=%s AND COL_NUM=%s"
        val=(user,row,column)
        mycursor.execute(sql, val)
        mydb.commit()