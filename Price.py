import mysql.connector
class Price:
    def price_set(self,num_of_rows,num_of_columns):
        mydb = mysql.connector.connect(user='admin', password='root', host='localhost', database='BOOKMYMOVIE')
        mycursor = mydb.cursor()
        total_seats=num_of_columns*num_of_rows
        if total_seats>60:
            first_half=(num_of_rows//2)
            second_half=num_of_rows-first_half
            second_half=second_half+65
            second_half_ascii=chr(second_half)
            sql="UPDATE BOOKINGS SET PRICE=8 WHERE ROW_NUM>=%s"
            val=(second_half_ascii,)
            mycursor.execute(sql,val)
            mydb.commit()