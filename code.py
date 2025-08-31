#importing mysql.connector
import mysql.connector as myc
# Opening a connection to MySQL Database
mys=myc.connect(host="localhost",user="root",passwd="root",database="practicle")
# Testing the whether connection is successful or not
if mys.is_connected()==True:
    print("connection established")
else:
    print("connection not established")
#creating cursor
cur=mys.cursor()
#functions starts from here
def new_reservation():
    #inserting new record to table
    print("############################################################")
    print("############################################################")
    print("##             **** Railway Reservation system **** ##")
    print("#                    New Reservation Data Entry Screen           #")
    print("################################################################")
    pnr1=input("Enter PNR(passenger name record) : ")
    name1=input("Enter Name : ")
    age1=int(input("Enter your age :"))
    berth_preference1=input("enter berth preference :")
    date_of_booking1=input("Enter Date(yyyy-mm-dd) of Booking : ")
    travelling_date1=input("Enter Date (yyyy-mm-dd) for booking : ")
    data="insert into reservation(pnr,name,age,berth_preference,dat_of_booking,travelling_date)
    values('{}','{}','{}','{}','{}','{}')".format(pnr1,name1,age1,berth_preference1,date_of_booking1,travelling_date1)
    cur.execute(data)
    
# Committing the changes made to table
    mys.commit()
    print("Reservation is Successful....")
# Function new_reservation is OVER


def get_info():
    #it will be done by fetching record
    command="select * from reservation"
    #executing the command
    cur.execute(command)
    print("############################################################")
    print("############################################################")
    print("##             Railway Reservation System                ##")
    print("##             Railway Reservation details                  ##")
    print("=============================================================")
    print("PNR","  Name","\t\tage","berth_pref","booking_dt","Travelling_dt")
    print("=============================================================")
    #Extracting Data from the cursor one by one using fetch(...) function
    details=cur.fetchone()
    while details:
        for i in details:
            print(i,end="\t")
            print()
            details=cur.fetchone()
    print("############################################################")
#function getinfo is OVER


import random
def cancel_reservation():
    print("############################################################")
    print("############################################################")
    print("##             Railway Reservation System                ##")
    print("##             Reservation cancellation Screen             ##")
    print("==========================================================")
    pnr1=input("Enter pnr :")
    details="Select * from reservation where pnr='{}'".format(pnr1)
    cur.execute(details)
    data=cur.fetchone()
    if data==None:
        print("NO such reservation is made")
        print("Plz Try again with a valid PNR..")
    else:
        y=random.randint(100,999)#Making the OTP
        print("your one time password:",y)
        n=int(input("Enter one time psssword:"))
        if n==y:
            print("cancelling reservation...")
            print(data)
            k=input("press ENTER key to proceed...")
            cur.execute("delete from reservation where pnr = {}".format(pnr1))
            mys.commit()
            print("Reservation Successfully cancelled ...")
        else:
            print("your entered otp didn't match...")
            print("retry...")
#cancel_reservation is OVER


def ModiRes():
    print("############################################################")
    print("############################################################")
    print("##             Railway Reservation System                ##")
    print("##             Reservation modification Screen            ##")
    print("===========================================================")
    pnr1=input("Enter pnr :")
    command = "Select * from reservation where pnr = {}".format(pnr1)
    cur.execute(command)
    data=cur.fetchone()
    if data==None:
        print("No such reservation exist..")
        print("Plz Try again with a valid pnr..")
    else:
        print("\nFollowing Reservation is being Modified\n")
        print(data)
        k=input("\nPress ENTER key to Proceed....")
        print("\n **** Now Enter New Details  ****")
        name=input("Enter Name :")
        age=int(input("Enter your age :"))
        berth_preference=input("enter berth preference :")
        date_of_booking=input("Enter Date(yyyy-mm-dd) of Booking : ")
        Travelling_date=input("Enter Date (yyyy-mm-dd) For booking : ")
        k=input("Press ENTER key to Proceed....")
        #command for update
        command="update reservation set name='{}',age={},berth_preference='{}',date_of_booking='{}',Travelling_date='{}' where pnr='{}'".format(name,age,berth_preference,date_of_booking,Travelling_date,pnr1)
        #executing command
        cur.execute(command)
        mys.commit()
        print("\nReservation Successfully Modified ...")
        
        
#main program
while True:
    print("############################################################")
    print("############################################################")
    print("                     W E L C O M E                          ")
    print("##             Rilway Reservation system                ##")
    print("############################################################")
    print("#################  MAIN-MENU  ###########################")
    print("############################################################")
    print("### 1.........................apply for reservation     ###")
    print("### 2.........................show reservation records  ###")
    print("### 3.........................cancel reservation        ###")
    print("### 4.........................update reservation Record ###")
    print("### 5.........................Exit                       ###")
    print("############################################################")
    print("############################################################")
    ch=int(input("\n\t Enter Your Choice(1..5) :"))
    print("############################################################")
    if ch==1:
        new_reservation()
    elif ch==2:
        get_info()
    elif ch==3:
        cancel_reservation()
    elif ch==4:
        ModiRes()
    elif ch==5:
        mys.close()
        break
    else:
        print("Invalid Choice ...plz enter a valid choice .")
        k=input("Press enter key to go to Main Menu....") # to hold the screen
