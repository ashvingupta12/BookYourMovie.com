import mysql.connector
class User:
    def show_user_info(self,row_u,col_u):
        mydb = mysql.connector.connect(user='admin', password='root', host='localhost', database='BOOKMYMOVIE')
        mycursor = mydb.cursor()
        sql="SELECT A.*,B.PRICE FROM USER A,BOOKINGS B WHERE B.ROW_NUM=%s and B.COL_NUM=%s"
        val=(row_u,col_u)
        mycursor.execute(sql,val)
        user_data=mycursor.fetchall()
        return user_data
