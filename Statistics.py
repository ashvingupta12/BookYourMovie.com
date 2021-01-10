import mysql.connector
class Statictics:
    def show_statis(self):
        mydb = mysql.connector.connect(user='admin', password='root', host='localhost', database='BOOKMYMOVIE')
        mycursor = mydb.cursor()
        sql = "SELECT COUNT(1) FROM BOOKINGS WHERE SEAT_STATUS='B' UNION SELECT COUNT(1) FROM BOOKINGS UNION SELECT SUM(PRICE) FROM BOOKINGS UNION SELECT SUM(PRICE) FROM BOOKINGS WHERE SEAT_STATUS='B'"
        mycursor.execute(sql)
        statis_result=mycursor.fetchall()
        return statis_result