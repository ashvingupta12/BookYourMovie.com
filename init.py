import mysql.connector
from Price import Price
class init:
    def init(self,num_of_rows,num_of_columns):
        mydb = mysql.connector.connect(user='admin', password='root', host='localhost', database='BOOKMYMOVIE')
        mycursor = mydb.cursor()
        ascii=65
        mycursor.execute("DELETE FROM BOOKINGS")
        mycursor.execute("DELETE FROM USER")
        for row in range(1,num_of_rows+1):
            row_alpha=chr(ascii)
            ascii+=1
            for col in range(1,num_of_columns+1):
                val=("WONDER WOMAN 1984","BS1",row_alpha,col,10,'S','None')
                sql = "INSERT INTO BOOKINGS VALUES (%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(sql,val)
        mydb.commit()
        price_obj=Price()
        price_obj.price_set(num_of_rows,num_of_columns)