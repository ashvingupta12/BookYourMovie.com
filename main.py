from init import init
from User import User
from Seat import Seat
from Statistics import Statictics
class main():
    def main_func(self):
        num_of_rows=int(input("Enter the number of rows:"))
        num_of_columns=int(input("Enter the number of seats in each row:"))
        init_obj=init()
        init_obj.init(num_of_rows,num_of_columns)
        self.show_options(num_of_columns)
    def show_options(self,num_of_columns):
        print("1.show the seats")
        print("2.Buy a Ticket")
        print("3.statictics")
        print("4.Show booked tickets user Info")
        print("5.Exit")
        option=int(input("Enter:"))
        if option==1:
            self.show_seats(num_of_columns)
        if option==2:
            self.buy_ticket(num_of_columns)
        if option==3:
            self.show_statistics(num_of_columns)
        if option==4:
            self.show_user_info(num_of_columns)
        if option==5:
            exit(0)
    def show_seats(self,num_of_columns):
        seat_obj = Seat()
        result=seat_obj.show_seats()
        dict={}
        for i in result:
            if i[0] not in dict.keys():
                dict[i[0]]=[]
                dict[i[0]].append(i[2])
            else:
                dict[i[0]].append(i[2])
        for col in range(1,num_of_columns+1):
            if col==1:
                print(" ",end=' ')
            print(col,end=' ')
        print("")
        for row in dict.keys():
            print(row,end=' ')
            for seat in dict[row]:
                print(seat,end=' ')
            print("")
        self.show_options(num_of_columns)
    def buy_ticket(self,num_of_columns):
        row_b=input("Enter the row:")
        col_b=input("Enter the column:")
        seat_obj = Seat()
        result=seat_obj.book_seat(row_b,col_b)
        if result[0][0]=='S':
            print("Seat is available for price ",result[0][1])
            conf=input("please type YES to confirm booking:")
            if conf=="YES":
                seat_obj.update_seat(row_b,col_b)
                print("Ticket booked succesfully")
                self.show_options(num_of_columns)
            else:
                self.show_options(num_of_columns)
        else:
            print("Seat is not avaiable")
            self.show_options(num_of_columns)
    def show_statistics(self,num_of_columns):
        sta_obj = Statictics()
        statis_result=sta_obj.show_statis()
        sold_count=statis_result[0][0]
        total_tickets=statis_result[1][0]
        total_income=statis_result[2][0]
        curr_income=statis_result[3][0]
        if curr_income==None:
            curr_income=0
        print("Number of purchased tickets:",sold_count)
        percentage=(sold_count/total_tickets)*100
        print("Percentage:",percentage,"%")
        print("current income:",curr_income)
        print("Total income:",total_income)
        self.show_options(num_of_columns)
    def show_user_info(self,num_of_columns):
        row_u=input("Enter row:")
        col_u=input("Enter col number")
        user_obj = User()
        user_data=user_obj.show_user_info(row_u,col_u)
        if user_data:
            print("Name:",user_data[0][0])
            print("Gender:", user_data[0][1])
            print("Age:", user_data[0][2])
            print("Ticket Price:", user_data[0][4])
            print("Phone No:", user_data[0][3])
            self.show_options(num_of_columns)
        else:
            print("Seat is not booked yet")
            self.show_options(num_of_columns)
main_obj=main()
main_obj.main_func()