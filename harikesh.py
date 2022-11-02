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
cur.execute('drop database railway')
cur.execute('create database if not exists railway')
cur.execute('use railway')

#creating table for train and passenger details
cur.execute("create table if not exists passenger_dtls(pname varchar(30),train_no int primary key,no_of_psng int,cls varchar(10),destination varchar(15),ticket_cost int,pnrno varchar(10))")
cur.execute("create table if not exists train_dtls(tname varchar(30),train_no int,station varchar(15),destination varchar(20),ticket_cost int,ecn int,ac int,slp int)")

#Defining menu function 
def menu():
     while True:
          print('\nWelcome To Railway some shit')
          print("Press")
          print("1 To Show Train Details")
          print("2 To Show Passenger Details")
          print("3 To Add New Passenger Details")
          print("4 To Add New Train Details")
          print("5 For Reservation Of Ticket")
          print("6 For Cancellation Of Ticket")
          print("7 To Exit")
          print()
          choice=int(input('Enter your preferred choice:'))

          if choice==1:
               Display_TrainDetails()
          elif choice==2:
               Display_Passenger()
          elif choice==3:
               add_passenger()
          elif choice==4:
               add_traindetails()  
          else:
               print('Invalid choice Try again')
          
#adding passenger details
def add_passenger():
     try:
          c=con.cursor()
          pname=input('Enter Passenger Name:')
          train_no=input("Enter Train No:")
          no_of_psng=input('Enter No.of Passengers:')
          cls=input('Enter Ticket Class:')
          destination=input('Enter Destination:')
          ticket_cost=input("Enter Fare:")
          pnrno=input("Enter pnrno:")
          data=(pname, train_no, no_of_psng, cls, destination, ticket_cost, pnrno)

          #inserting passenger details 
          sql='insert into passenger_dtls values(%s,%s,%s,%s,%s,%s,%s)'

          #Executing SQL query
          c.execute(sql,data)

          #commit() methods to make changes
          con.commit()
          print("Passenger Added Successfully")
          menu()
     except:
          print("Enter correct values!!")

#To add details of a new train
def add_traindetails():
     try:
          c=con.cursor()
          tname=input('Enter Train Name:')
          train_no=input("Enter Train No:")
          station=input("Enter Station Name:")
          destination=input('Enter Destination:')
          ticket_cost=input("Enter Fare:")
          ecn=input("Enter no.of seats for economy:")
          ac=input("Enter no.of seats for ac:")
          slp=input("Enter no.of seats for sleeper:")
          data=(tname, train_no, station, destination, ticket_cost, ecn, ac, slp)

          sql='insert into train_dtls values(%s,%s,%s,%s,%s,%s,%s,%s)'

          c.execute(sql,data)

          con.commit()
          print("Train Details Added Successfully")
          menu()
     except:
          print("Enter correct values!!")

#Function to Display details of all the Passengers
def Display_Passenger():
     sql='select*from passenger_dtls'
     c=con.cursor()

     c.execute(sql)
     
     r=c.fetchall()
     print()  
     print("Processing please wait....")
     import time
     time.sleep(3)
     print()
     print("Printing results....")
     time.sleep(2)
     print()
     for i in r:
          print("pname:", i[0],"train_no:", i[1],"no_of_psng:",i[2],"cls:",i[3],"destination:",i[4],"ticket_cost:",i[5],"pnrno:",i[6])

     menu()
def Display_TrainDetails():
    sql='select*from train_dtls'
    c=con.cursor()

    c.execute(sql)
     
    r=c.fetchall()
    print()
    print("Processing please wait....")
    import time
    time.sleep(3)
    print()
    print("Printing results....")
    time.sleep(2)
    print()
    for i in r:
        print("tname:",i[0],"train_no:",i[1],"station:",i[2],"destination:",i[3],"ticket_cost:",i[4],"ecn:",i[4],"ac:",i[5],"slp:",i[6])

    menu()

menu()
