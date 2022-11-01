print("                         RAILWAY MANAGEMENT                     ")


#importing mysqlconnector
import mysql.connector 
import pickle

#making connection
try:
     con=mysql.connector.connect(host="localhost", user = "root" , password = "qwerty")
except:
     print("Connection Error")

#allows row-by-row processing of the result sets
cur=con.cursor()

#creating a database
cur.execute('create database emp')
cur.execute('use emp')

#creating table for train details
cur.execute("create table if not exists passenger_dtls(pname varchar(30),train_no int primary key,no_of_psng int,cls varchar(5),destination varchar(15),ticket_cost int,pnrno varchar(5))")

#Defining menu function 
def menu():
     while True:
          print('\nWelcome To Railway some shit')
          print("Press")
          print("1 To Show Train Details")
          print("2 To Show All Active Passengers")
          print("3 To Add New Passenger Details")
          print("4 To Add New Train Details")
          print("5 For Reservation Of Ticket")
          print("6 For Cancellation Of Ticket")
          print("7 To Exit")
          print()
          choice=int(input('Enter your preferred choice:'))
          
          if choice==1:
               hehe
          elif choice==2:
               boi
          elif choice==3:
               add_passenger()
          elif choice==4:
               suiii
          elif choice==5:
               brrrrr
          elif choice==6:
               why u gae
          elif choice==7:
               sys.exit()
          else:
               print('Invalid choice Try again')
          
#adding passenger details
def add_passenger():
     c=con.cursor()
     pname=input('Enter Passenger Name:')
     train_no=imput("Enter Train No:")
     no_of_psng=input('Enter No.of Passengers:')
     cls=input('Enter Ticket Class:')
     destination=input('Enter Destination:')
     ticket_cost=input("Enter Fare:")
     pnrno=input("Enter pnrno:")
     data=(pname, train_no, no_of_psng, cls, destination, ticket_cost, pnrno)

     #inserting passenger details 
     sql=insert into passenger_dtls(pname,train_no,no_of_psng,cls,destination,ticket_cost,pnrno)values(%s,%s,%s,%s,%s,%s,%s)

     #Executing SQL query
     c.execute(sql,data)

     #commit() methods to make changes
     con.commit()

     print("Employee Added Successfully")



