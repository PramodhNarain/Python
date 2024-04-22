# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:28:58 2024

@author: Pramodh Narain
"""
#Mini-Project-2nd-Sem-Pramodh
#Topic: Airline-Ticket-Booking
#Code-Name: Easy2BookNFly

import sys
import csv
import time
import random
import datetime
today = datetime.date.today()
year = today.year
month = today.month
day = today.day
import mysql.connector as connector
connection_string = connector.connect (host = "localhost", user = "root", passwd = "MySQL_1_2_3")
cursor_object = connection_string.cursor()

def print_text(x):
    
    for g in x+'\n':

        sys.stdout.write(g)
        sys.stdout.flush()
        time.sleep(1./50)
    
    return ""

print_text("Hello User :)")
print_text("Easy2BookNFly gives you a warm welcome!! :)")
print_text("This code allows you to book an airline ticket based on the data you provide as input.")

def Domestic_Budget_Choice():
    
    global Airline, Budget_price, airline_choice
    Budget_price = 0
    
    if Budget_choice == 1:
        
        while True:
            
            try:
                
                print_text("The domestic flights available in the price range of Rs.30,000 to Rs.50,000 are displayed as follows:")
                print_text("1. Spicejet")
                print_text("2. Akasa Air")
                airline_choice = int(input(print_text("Enter your choice from the above menu (1/2): ")))
                break
            
            except ValueError:
                
                print_text("Expected integer data type!")
        
        Airline = " "
        
        while True:
            
            if airline_choice == 1:
                Airline += "Spicejet"
                Budget_price += 30000
                break
            
            elif airline_choice == 2:
                Airline += "Akasa Air"
                Budget_price += 50000
                break
            
            else:
                print_text("Invalid Choice! Please try again!")
    
    elif Budget_choice == 2:
        
        while True:
            
            try:
                
                print_text("The domestic flights available in the price range of Rs.60,000 to Rs.80,000 are displayed as follows:")
                print_text("1. Air India")
                print_text("2. Indigo")
                airline_choice = int(input(print_text("Enter your choice from the above menu (1/2): ")))
                break
            
            except ValueError:
                
                print_text("Expected integer data type!")
        
        Airline = " "
        
        while True:
            
            if airline_choice == 1:

                Airline += "Air India"
                Budget_price += 60000
                break
            
            elif airline_choice == 2:

                Airline += "Indigo"
                Budget_price += 80000
                break
            
            else:

                print_text("Invalid Choice! Please try again!")
                
    elif Budget_choice == 3:
        
        while True:
            
            try:
                
                print_text("The domestic flights available in the price range of Rs.90,000 to Rs.100,000 are displayed as follows:")
                print_text("1. Vistara")
                print_text("2. Air India Express")
                airline_choice = int(input(print_text("Enter your choice from the above menu (1/2): ")))
                break
            
            except ValueError:
                
                print_text("Expected integer data type!")
                
        Airline = " "
        
        while True:
            
            if airline_choice == 1:

                Airline += "Vistara"
                Budget_price += 90000
                break
            
            elif airline_choice == 2:

                Airline += "Air India Express"
                Budget_price += 100000
                break
            
            else:

                print_text("Invalid Choice! Please try again!")
        
    elif Budget_choice == 4:
        
        while True:
            
            try:
                
                print_text("The domestic flights available in the price range of Rs.110,000 to Rs.150,000 are displayed as follows:")
                print_text("1. Go First")
                print_text("2. Air Asia India")
                airline_choice = int(input(print_text("Enter your choice from the above menu (1/2):")))
                break
            
            except ValueError:
                
                print_text("Expected integer data type!")
                
        Airline = " "
        
        while True:
            
            if airline_choice == 1:

                Airline += "Go First"
                Budget_price += 110000
                break
            
            elif airline_choice == 2:

                Airline += "Air Asia India"
                Budget_price += 150000
                break
            
            else:

                print_text("Invalid Choice! Please try again!")
                
    else:

        print_text("Invalid Choice! Please try again!")
        return

#Insert Method:
def Domestic_Flights():
    
    global Customer_ID,number,First_Name,Last_Name,Age,Date_of_Birth,Airline,Budget_Choice,Start_Location,End_Location,Seating_Position,Seat_Number,Date,Time,Class
    
    Customer_ID = random.randrange (300000 , 900000 , 1)
    print_text("Customer ID for this passenger is : ")
    print_text(str(Customer_ID))
    First_Name = input(print_text("Enter first name of the passenger : "))
    Last_Name = input(print_text("Enter last name of the passenger : "))
    print_text("WARNING!! : ")
    print_text("Age and Date of Birth can be given as input only once and cannot be modified once entered. Hence, please be alert while entering the data!")
    
    while True:
        
        try:
            
            Age = int(input(print_text("Enter age of the passenger:")))
            break
        
        except ValueError:
            
            print_text("Expected integer data type!")
    
    while True:
        
        Date_of_Birth = input(print_text("Enter date of birth of the passenger (Format: (yyyy/mm/dd)):"))
        
        if ((int(Date_of_Birth[0:4]) + Age)) != year:
            
            print_text("Invalid date of birth/Invalid age")
            print_text("Please try again!")
        
        else:
            
            break

    def Domestic_Cost_of_Travel():
        
        global Airline, Budget_choice
        
        Airline = "  "
        
        while True:
            
            try:
                
                print_text("Choose your budget range from the dropdown menu:")
                print_text("1. Rs.30,000 to Rs.50,000")
                print_text("2. Rs.60,000 to Rs.80,000")
                print_text("3. Rs.90,000 to Rs.100,000")
                print_text("4. Rs.100,000 to Rs.150,000")
                Budget_choice = int(input(print_text("Enter your choice from above menu (1/2/3/4):")))
                break
            
            except ValueError:
                
                print_text("Expected integer data type!")
                
    Domestic_Cost_of_Travel()
    
    Domestic_Budget_Choice()
    
    global Start, End
    
    while True:
        
        print_text("Enter your start and end locations:")
        Start_Location = input(print_text("Enter start location:"))
        End_Location = input(print_text("Enter destination:"))
        Start = End = " "
        
        if Start_Location == End_Location:
            
            print_text("Start and End locations are same. Please enter location details properly!")
        
        else:
            
            Start += Start_Location
            End += End_Location
            break
        
    def Seating_Position():
        
        global Seating_Position
        Seating_Position = "  "
        
        while True:
            
            try:
                
                print_text("You can select your seating position as displayed in the following menu:")
                print_text("1. Aisle Seat")
                print_text("2. Middle Seat")
                print_text("3. Window Seat")
                break
            
            except ValueError:
                
                print_text("Expected integer data type!")
        
        while True:
            
            try:
                
                SP = int(input(print_text("Enter your choice from above menu (1/2/3):")))
                break
            
            except ValueError:
                
                print_text("Expected integer data type!")
        
        while True:
            
            Seating_Position = " "
            
            if SP == 1:
                
                Seating_Position += "Aisle Seat"
                break
            
            elif SP == 2:
                
                Seating_Position += "Middle Seat"
                break
            
            elif SP == 3:
                
                Seating_Position += "Window Seat"
                break
            
            else:
                
                print_text("Invalid Choice! Please try again!")
                
        return Seating_Position
    
    Seating_Position()
    
    def Seat_Number():
        
        global Seat_Number
        
        Seat = random.randrange (65,91,1)
        Number = random.randrange (1,501,1)
        Seat_Number = chr(Seat) + str(Number)
        print_text("Your Seat Number is displayed as follows : ")
        print_text(Seat_Number)
        return Seat_Number
    
    Seat_Number()
     
    def Date_Of_Travel():
        
        print_text("WARNING!!: Date of travel once given as input cannot be modified later. So make sure you follow the appropriate syntax as given within the parentheses")
        
        global Date
        
        while True:
            
            Date=input(print_text("Enter desired date of travel (Format: (yyyy/mm/dd)):"))
            
            if str(year)<Date[0:4] or str(month)<Date[5:7] or str(day)<Date[8:10]:
                
                print_text("Invalid date! Please enter valid date!")
                
                if Date[5:7]=="02":
                    
                    if int(Date[8:10])>28:
                        
                        print_text("Invalid date! Please enter valid date!")
                    
                    elif Date[5:7]=="01" or Date[5:7]=="03" or Date[5:7]=="05" or Date[5:7]=="07" or Date[5:7]=="08" or Date[5:7]=="10" or Date[5:7]=="12":
                        
                        if int(Date[8:10])>31:
                            
                            print_text("Invalid date! Please enter valid date!")
                    
                    elif Date[5:7]=="01" or Date[5:7]=="04" or Date[5:7]=="06" or Date[5:7]=="09" or Date[5:7]=="11":
                        
                        if int(Date[8:10])>30:
                            
                            print_text("Invalid date! Please enter valid date!")                                
            
            else:
                
                break
            
            break
    
    Date_Of_Travel()

    def Time():
        
        global Time
        
        Time = "  "
        
        while True:

            try:

                print_text("The available timings of your selected flight are displayed as follows:")
                print_text("1. 2:00 AM")
                print_text("2. 9:00 AM")
                print_text("3. 3:00 PM")
                print_text("4. 9:00 PM")
                break 

            except ValueError:

                print_text("Expected integer data type!")

        while True:

            try:

                choice=int(input(print_text("Enter your choice from above menu (1/2/3/4):")))
                break

            except ValueError:

                print_text("Expected integer data type!")
        
        Time="  "

        while True:

            if choice == 1:

                Time += "2:00 AM"
                break

            elif choice == 2:

                Time += "9:00 AM"
                break

            elif choice == 3:

                Time += "3:00 PM"
                break

            elif choice == 4:

                Time += "9:00 PM"
                break

            else:

                print_text("Invalid Choice! Please try again!")
        
        return
    
    Time()


    def Class():

        global Class

        while True:

            try:

                print_text("Choose the class of flight you want to travel in from following menu:")
                print_text("1. Business Class")
                print_text("2. Economy Class")
                break

            except ValueError:

                print_text("Expected integer data type!")

        while True:

            try:

                choice=int(input(print_text("Enter your choice from above menu (1/2):")))
                break

            except ValueError:

                print_text("Expected integer data type!")

        Class=" "

        while True:

            if choice==1:

                Class += "Business Class"
                break

            elif choice==2:

                Class += "Economy Class"
                break


    Class()

    
    print_text("Successfully recorded one passenger information.")
    loop=False
       
        
def International_Budget_Choice():

    global Airline,Budget_price,inner_choice

    Budget_price=0

    if Budget_choice==1:

        while True:

            try:

                print_text("The international flights available in the price range of Rs.100,000 to Rs.150,000 are displayed as follows:")
                print_text("1.British Airways")
                print_text("2.Jet Airways")
                inner_choice=int(input(print_text("Enter your choice from above menu (1/2):")))
                break

            except ValueError:

                print_text("Expected integer data type!")


        Airline=" "

        while True:

            if inner_choice==1: 

                Airline += "British Airways"
                Budget_price += 100000
                break

            elif inner_choice==2:

                Airline += "Jet Airways"
                Budget_price += 145000
                break

            else:
                
                print_text("Invalid Choice! Please try again!")


    elif Budget_choice==2:

        while True:

            try:

                print_text("The international flights available in the price range of Rs.160,000 to Rs.200,000 are displayed as follows:")
                print_text("1.Air China Flights")
                print_text("2.Aeroflot Airline")
                inner_choice=int(input(print_text("Enter your choice from above menu (1/2):")))
                break

            except ValueError:

                print_text("Expected integer data type!")


        Airline=" "

        while True:

            if inner_choice==1:

                Airline += "Air China Flights"
                Budget_price += 160000
                break

            elif inner_choice==2:

                Airline += "Aeroflot Airline"
                Budget_price += 200000
                break

            else:

                print_text("Invalid Choice! Please try again!")


    elif Budget_choice==3:

        while True:

            try:

                print_text("The international flights available in the price range of Rs.250,000 to Rs.300,000 are displayed as follows:")
                print_text("1. Austrian Airlines")
                print_text("2. Cathay Pacific Airlines")
                inner_choice = int(input(print_text("Enter your choice from above menu (1/2):")))
                break

            except ValueError:

                print_text("Expected integer data type!")
        
        Airline="  "
        
        while True:
        
            if inner_choice==1:
        
                Airline += "Austrian Airlines"
                Budget_price += 250000
                break
        
            elif inner_choice==2:
        
                Airline += "Cathay Pacific Airlines"
                Budget_price += 300000
                break
        
            else:
                print_text("Invalid Choice! Please try again!")
    
    elif Budget_choice==4:

        while True:
        
            try:
        
                print_text("The international flights available in the price range of Rs.350,000 to Rs.400,000 are displayed as follows:")
                print_text("1.Emirates Airlines")
                print_text("2.Delta Airlines")
                inner_choice=int(input(print_text("Enter your choice from above menu (1/2):")))
                break
        
            except ValueError:
        
                print_text("Expected integer data type!")
        
        Airline=" "
        
        while True:
        
            if inner_choice==1:

                Airline += "Emirates Airlines"
                Budget_price += 350000
                break
        
            elif inner_choice==2:

                Airline += "Delta Airlines"
                Budget_price += 400000
                break
        
            else:
        
                print_text("Invalid Choice! Please try again!")
        
        else:
        
            print_text("Invalid choice! Please try again!") 
            

#Insert Method:
def International_Flights():

    global Customer_ID,Number,First_Name,Last_Name,Age,Date_of_Birth,Airline,Budget_Choice,Start_Location,End_Location,Seating_Position,Seat_Number,Date,Time,Class
    
    Customer_ID=random.randrange(300000,900000,1)
    print_text("Customer ID for this passenger is:")
    print_text(str(Customer_ID))
    First_Name = input(print_text("Enter first name of the passenger:"))
    Last_Name = input(print_text("Enter last name of the passenger:"))
    print_text("WARNING!!:")
    print_text("Age and Date of Birth can be given as input only once and cannot be modified once entered. Hence, please be alert while entering the data!")
    
    while True:
    
        try:
    
            Age=int(input(print_text("Enter age of the passenger:")))
            break
    
        except ValueError:
    
            print_text("Expected integer data type!")
    
    while True:
    
        Date_of_Birth=input(print_text("Enter date of birth of the passenger (Format: (yyyy/mm/dd)):"))
    
        if ((int(Date_of_Birth[0:4])+Age))!=year:
    
            print_text("Invalid date of birth/Invalid age")
            print_text("Please try again!")
    
        else:
    
            break
    
    
    def International_Cost_of_Travel():
    
        global Airline, Budget_price, Budget_choice
    
        Airline=" "
    
        while True:
    
            try:
    
                print_text("Choose your budget range from the dropdown menu:")
                print_text("1.Rs.100,000 to Rs.150,000")
                print_text("2.Rs.160,000 to Rs.200,000")
                print_text("3.Rs.250,000 to Rs.300,000")
                print_text("4.Rs.350,000 to Rs.400,000")
                break
    
            except ValueError:
    
                print_text("Expected integer data type!")
    
    
        while True:
    
            Budget_price=0
    
            try:
    
                Budget_choice=int(input(print_text("Enter your choice from above menu(1/2/3/4):")))
                break
    
            except ValueError:
    
                print_text("Expected integer data type!")
    
    
    International_Cost_of_Travel()
    
    International_Budget_Choice()
    
    while True:
    
        print_text("Enter your start and end locations:")
        Start_Location = input(print_text("Enter start location:"))
        End_Location=input(print_text("Enter destination:"))
        
        Start=End=" "
        
        if Start_Location==End_Location:
        
            print_text("Start and End locations are same. Please enter location details properly!")
        
        else:
        
            Start += Start_Location
            End += End_Location
            break
    
    Seating_Position=" "
    
    while True:
    
        try:
    
            print_text("You can select your seating position as displayed in the following menu:")
            print_text("1.Aisle Seat")
            print_text("2.Middle Seat")
            print_text("3.Window Seat")
            SP=int(input(print_text("Enter your choice from above menu (1/2/3):")))
            break
    
        except ValueError:
    
            print_text("Expected integer data type!")
    
    while True:
    
        if SP==1:
    
            Seating_Position += "Aisle Seat"
            break
    
        elif SP==2: 
    
            Seating_Position += "Middle Seat"
            break
    
        elif SP==3:
    
            Seating_Position += "Window Seat"
            break
    
        else:
    
            print_text("Invalid Choice! Please try again!")
    
    Seat = random.randrange(65,91,1)
    Number = random.randrange(1,51,1)
    Seat_Number = chr(Seat) + str(Number)
    print_text("Your Seat Number is displayed as follows:")
    print_text(Seat_Number)    
    
    def Date_Of_Travel():
    
        print_text("WARNING!!: Date of travel once given as input cannot be modified later. So make sure you follow the appropriate syntax as given within the parentheses")
    
        global Date
    
        while True:
    
            Date=input(print_text("Enter desired date of travel (Format: (yyyy/mm/dd)):"))
    
            if str(year)<Date[0:4] or str(month)<Date[5:7] or str(day)<Date[8:10]:
    
                print_text("Invalid date! Please enter valid date!")
    
                if Date[5:7]=="02":
    
                    if int(Date[8:10])>28:
    
                        print_text("Invalid date! Please enter valid date!")
    
                elif Date[5:7]=="01" or Date[5:7]=="03" or Date[5:7]=="05" or Date[5:7]=="07" or Date[5:7]=="08" or Date[5:7]=="10" or Date[5:7]=="12":
    
                    if int(Date[8:10])>31:
    
                        print_text("Invalid date! Please enter valid date!")
    
                elif Date[5:7]=="04" or Date[5:7]=="06" or Date[5:7]=="09" or Date[5:7]=="11" or Date[5:7]=="11":
    
                    if int(Date[8:10])>30:
    
                                print_text("Invalid date! Please enter valid date!")                                
    
                else:
    
                    break
    
                break
            break
    
    
    Date_Of_Travel()
                    
    
    while True:
    
        try:
    
            print_text("The available timings of your selected flight are displayed as follows:")
            print_text("1. 2:00 AM")
            print_text("2. 9:00 AM")
            print_text("3. 3:00 PM")
            print_text("4. 9:00 PM")
    
            choice = int(input(print_text("Enter your choice from above menu (1/2/3/4):")))
    
            break

        except ValueError:
        
            print_text("Expected integer data type!")
    
    
    while True:

        Time="  "
        
        if choice==1:
        
            Time += "2:00 AM"
            break
        
        elif choice==2:
        
            Time += "9:00 AM"
            break
        
        elif choice==3:
        
            Time += "3:00 PM"
            break
        
        elif choice==4:
        
            Time += "9:00 PM"
            break
        
        else:
        
            print_text("Invalid Choice! Please try again!")
    
    while True:
        
        try:
        
            print_text("Choose the class of flight you want to travel in from following menu:")
            print_text("1.Business Class")
            print_text("2.Economy Class")
            choice=int(input(print_text("Enter your choice from above menu (1/2):")))
            break
        
        except ValueError:
        
            print_text("Expected integer data type!")
    
    while True:
        
        Class=" "
        
        if choice==1:
        
            Class += "Business Class"
            break
        
        elif choice==2:
        
            Class += "Economy Class"
            break
        
        else:
        
            print_text("Invalid choice! Please try again!")
    
    
    print_text("Successfully recorded one passenger information.")
      

def Payment():

    print_text("Now we will guide you with the payment procudure as follows:")
    
    while True:
    
        try:
    
            print_text("Choose a method of payment from the dropdown list as displayed below:")
            print_text("1.Credit card")
            print_text("2.Debit card")
            choice=int(input(print_text("Enter your choice from the above menu (1/2):")))
            break
    
        except ValueError:
    
            print_text("Expected integer data type!")
    
    if choice==1:
    
        Customer_ID=int(input(print_text("Enter customer ID:")))
    
        while True:
    
            Phone_Number=int(input(print_text("Enter phone number:")))
            Ph_Str=str(Phone_Number)
    
            if len(Ph_Str)==10:
    
                break
    
            else:
    
                print_text("Invalid Phone number!")
                print_text("Please try again!")
    
        print_text("Generating OTP.....")
        print_text("Your OTP is displayed as follows:")
    
        while True:
    
            PIN=random.randrange(100000,1000000,1)
            print_text(str(PIN))
            OTP=int(input(print_text("Enter OTP:")))
    
            if OTP==PIN:
    
                print_text("Your payment has been receieved by us.")
                print_text("Thank you for your cooperation!! Have a nice day!")
                break
    
            else:
    
                print_text("Incorrect OTP entered. Please try again!")
    
    
    elif choice==2:
    
        Card_NO=int(input(print_text("Enter your card number ")))
    
        while True:
    
            Phone_Number=int(input(print_text("Enter phone number:")))
            Ph_Str=str(Phone_Number)
    
            if len(Ph_Str)==10:
    
                break
    
            else:
    
                print_text("Invalid Phone number!")
                print_text("Please try again!")
    
        print_text("Generating OTP.....")
        print_text("Your OTP is displayed as follows:")
    
        while True:
    
            PIN=random.randrange(100000,1000000,1)
            print_text(str(PIN))
            OTP=int(input(print_text("Enter OTP:")))
    
            if OTP==PIN:
    
                print_text("Your payment has been receieved by us.")
                print_text("Thank you for your cooperation!! Have a nice day!")
                break
    
            else:
    
                print_text("Incorrect OTP entered. Please try again!")
    
    else:
    
        print_text("Invalid Choice! Please try again!")



def Delete():

    global Customer_ID, choice
    
    cursor_object.execute("USE Airline_Ticket ;")

    while True:

        try:

            print_text("Select any one table from following:")
            print_text("1.Domestic_Flight_Ticket")
            print_text("2.International_Flight_Ticket")
            choice=int(input(print_text("Enter your choice from above menu (1/2):")))
            break

        except ValueError:
        
            print_text("Expected integer data type!")
    
    if choice==1:

        Customer_ID=int(input(print_text("Enter Customer ID according to which you wish to delete the ENTIRE passenger details:")))
        Customer_ID_STR=str(Customer_ID)
        print_text("We shall be displaying the existing records in the table for your convinience while deleting the tuple's data.")
        print_text("The content present in the table 'Domestic_Flight_Ticket' is displayed as follows:")
        Selection_Query=str("SELECT * FROM Domestic_Flight_Ticket WHERE Customer_ID="+Customer_ID_STR+";")
        cursor_object.execute(Selection_Query)

        for record in cursor_object:

            print_text(str(record))
        
        connection_string.commit()  
    
    elif choice==2:

        Customer_ID=int(input(print_text("Enter Customer ID according to which you wish to delete the ENTIRE passenger details:")))
        Customer_ID_STR=str(Customer_ID)
        print_text("We shall be displaying the existing records in the table for your convinience while deleting the tuple's data.")
        print_text("The content present in the table 'Domestic_Flight_Ticket' is displayed as follows:")
        Selection_Query=str("SELECT * FROM International_Flight_Ticket WHERE Customer_ID="+Customer_ID_STR+";")
        cursor_object.execute(Selection_Query)
        
        for record in cursor_object:
        
            print_text(str(record))
        
        connection_string.commit()


    if choice==1:

        inner_choice_1=input(print_text("Are you sure you wish to delete the ENTIRE passenger details ? (yes/no)"))
        
        if inner_choice_1.lower()=="yes":
        
            print_text("Deletion of passenger details is in progress...Please wait for sometime...")
            Customer_ID_STR=str(Customer_ID)
            Deletion_Query="Delete from Domestic_Flight_Ticket "+" where Customer_ID = "+Customer_ID_STR+";"
            cursor_object.execute(Deletion_Query)
            connection_string.commit()
            print_text("Passenger details have been successfully deleted from the table!!")
            Payment()
        
        elif inner_choice_1.lower()=="no":
        
            print_text("No worries, the passengers' details are safe. None of them have been deleted yet :)")
        
            Payment()
        
        else:
        
            print_text("No worries, the passengers' details are safe. None of them have been deleted yet :)")
        
            Payment()
        
    elif choice==2:

        inner_choice_2=input(print_text("Are you sure you wish to delete the ENTIRE passenger details ? (yes/no)"))
        
        if inner_choice.lower_2()=="yes":
        
            print_text("Deletion of passenger details is in progress...Please wait for sometime...")
            Customer_ID_STR=str(Customer_ID)
            Deletion_Query="Delete from International_Flight_Ticket "+" where Customer_ID = "+Customer_ID_STR+";"
            cursor_object.execute(Deletion_Query)
            connection_string.commit()
            print_text("Passenger details have been successfully deleted from the table!!")
        
            Payment()
        
        elif inner_choice_2.lower()=="no":
        
            print_text("No worries, the passengers' details are safe. None of them have been deleted yet :)")
        
            Payment()
        
        else:
        
            print_text("No worries, the passengers' details are safe. None of them have been deleted yet :)")
        
            Payment()


def Update():

    global Customer_ID, choice

    cursor_object.execute("USE Airline_Ticket ;")

    while True:

        try:

            print_text("Select any one table from following:")
            print_text("1.Domestic_Flight_Ticket")
            print_text("2.International_Flight_Ticket:")
            choice=int(input(print_text("Enter your choice from above menu (1/2):")))
            break

        except ValueError:

            print_text("Expected integer data type!")

    if choice==1:

        ID=int(input(print_text("Enter Customer ID according to which you wish to update the passenger's details:")))
        Customer_ID_STR=str(ID)
        print_text("We shall be displaying the existing records in the table for your convinience while updating the tuple's data.")
        print_text("The content present in the table 'Domestic_Flight_Ticket' is displayed as follows:")
        cursor_object.execute("USE Airline_Ticket;")
        Selection_Query="SELECT * FROM Domestic_Flight_Ticket WHERE Customer_ID="+Customer_ID_STR+";"
        cursor_object.execute(Selection_Query)

        for record in cursor_object:

            print_text(str(record))

        #connection_string.commit()  

    elif choice==2:

        ID=int(input(print_text("Enter Customer ID according to which you wish to delete the pssenger's details:")))
        Customer_ID_STR=str(ID)
        print_text("We shall be displaying the existing records in the table for your convinience while deleting the tuple's data.")
        print_text("The content present in the table 'International_Flight_Ticket' is displayed as follows:")
        cursor_object.execute("USE Airline_Ticket;")
        Selection_Query="SELECT * FROM International_Flight_Ticket WHERE Customer_ID="+Customer_ID_STR+";"
        cursor_object.execute(Selection_Query)

        for record in cursor_object:

            print_text(str(record))

        #connection_string.commit()

    if choice==1:

        while True:

            try:

                cursor_object.execute("USE Airline_Ticket;")
                print_text("Select one column from the following menu according to which you wish to update the passenger details.")
                print_text("Menu:")
                print_text("1.First_Name")
                print_text("2.Last_Name")
                print_text("3.Airline")
                print_text("4.Start_Location")
                print_text("5.End_Location")
                print_text("6.Seating_Position")
                print_text("7.Time")
                print_text("8.Class")
                column_choice=int(input(print_text("Select any one column from above menu (1/2/3/4/5/6/7/8):")))
                break

            except ValueError:

                print_text("Expected integer data type!")

        new_data=input(print_text("Enter new data to be modified in SQL table:"))

        filed_name=None

        if column_choice==1:

            field_name="First_Name"

        elif column_choice==2:

            field_name="Last_Name"

        elif column_choice==3:

            field_name="Airline"

        elif column_choice==4:

            field_name="Start_Location"

        elif column_choice==5:

            field_name="End_Location"

        elif column_choice==6:

            field_name="Seating_Position"

        elif column_choice==7:

            field_name="Time"

        elif column_choice==8:

            field_name="Class"

        Customer_ID_STR=str(Customer_ID)
        Updation_Query="Update Domestic_Flight_Ticket set "+field_name+" = "+"'"+new_data+"'"+" where Customer_ID= "+Customer_ID_STR+";"
        cursor_object.execute(Updation_Query)
        connection_string.commit()
        print_text("Passenger details have been successfully updated from the table!!")

        Payment()

    elif choice==2:

        while True:

            try:

                cursor_object.execute("USE Airline_Ticket;")
                print_text("Select one column from the following menu according to which you wish to delete the ENTIRE passenger details.")
                print_text("Menu:")
                print_text("1.First_Name")
                print_text("2.Last_Name")
                print_text("3.Airline")
                print_text("4.Start_Location")
                print_text("5.End_Location")
                print_text("6.Seating_Position")
                print_text("7.Time")
                print_text("8.Class")
                column_choice=int(input(print_text("Select any one column from above menu (1/2/3/4/5/6/7/8):")))
                break

            except ValueError:

                print_text("Expected integer data type!")

        new_data=input(print_text("Enter new data to be modified in SQL table:"))
        filed_name=None

        if column_choice==1:

            field_name="First_Name"

        elif column_choice==2:

            field_name="Last_Name"

        elif column_choice==3:

            field_name="Airline"

        elif column_choice==4:

            field_name="Start_Location"

        elif column_choice==5:

            field_name="End_Location"

        elif column_choice==6:

            field_name="Seating_Position"

        elif column_choice==7:

            field_name="Time"

        elif column_choice==8:

            field_name="Class"

        Customer_ID_STR=str(Customer_ID)
        Updation_Query="Update International_Flight_Ticket set "+field_name+" = "+"'"+(new_data)+"'"+" where Customer_ID= "+Customer_ID_STR+";"
        cursor_object.execute(Updation_Query)
        connection_string.commit()
        print_text("Passenger details have been successfully updated from the table!!")

        Payment()

    else:

        print_text("No worries, the passengers' details are safe. None of them have been modified yet :)")

        Payment()



#Insert Method        

def Choose_Region():

    global choice

    while True:

        try:

            print_text("Do you wish to travel within India or outside India?")
            print_text("1.Within India")
            print_text("2.Outside India")
            choice=int(input(print_text("Enter your choice (1/2):")))
            break

        except ValueError:

            print_text("Expected integer data type!")

    count=0

    while count==0:

        if choice==1:

            while True:

                try:

                    number=int(input(print_text("Enter number of passengers:")))
                    break

                except ValueError:

                    print_text("Expected integer data type!")

            for x in range(number):

                Domestic_Flights()

                cursor_object.execute("CREATE DATABASE IF NOT EXISTS Airline_Ticket;")
                cursor_object.execute("USE Airline_Ticket;")
                cursor_object.execute("""Create Table if not exists Domestic_Flight_Ticket (Customer_ID int unique, First_Name varchar(20) not null, Last_Name varchar(20) not null, 
                                      Age int not null, Date_of_Birth date not null, Airline varchar(25) not null,Start_location varchar(20) not null, 
                                      End_Location varchar(20) not null, Seating_Position varchar(20) not null,
                                    Seat_Number varchar(6) primary key,Date_of_Travel date not null, Time varchar(20) not null, Class varchar(20) not null);""")

                Table_Details=(Customer_ID,First_Name,Last_Name,Age,Date_of_Birth,Airline,Start_Location,End_Location,Seating_Position,Seat_Number,Date,Time,Class)

                Add_User="Insert into Domestic_Flight_Ticket values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

            cursor_object.execute(Add_User, Table_Details)

            connection_string.commit()

            count += 1 


        elif choice==2:

            while True:

                try:

                    number=int(input(print_text("Enter number of passengers:")))
                    break

                except ValueError:

                    print_text("Expected integer data type!:")

            for x in range(number):

                International_Flights()

                cursor_object.execute("CREATE DATABASE IF NOT EXISTS Airline_Ticket;")
                cursor_object.execute("USE Airline_Ticket;")
                cursor_object.execute("""Create Table if not exists International_Flight_Ticket (Customer_ID int unique, First_Name varchar(20) not null, 
                                      Last_Name varchar(20) not null, Age int not null, Date_of_Birth date not null,Airline varchar(25) not null,
                                      Start_location varchar(20) not null, End_Location varchar(20) not null, Seating_Position varchar(20) not null,
                                      Seat_Number varchar(6) primary key,Date_of_Travel date not null, Time varchar(20) not null, Class varchar(20) not null);""")

                Table_Details=(Customer_ID,First_Name,Last_Name,Age,Date_of_Birth,Airline,Start_Location,End_Location,Seating_Position,Seat_Number,Date,Time,Class)

                Add_User="Insert into International_Flight_Ticket values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

            cursor_object.execute(Add_User, Table_Details)

            connection_string.commit()

            count += 1


        elif choice != 1 and choice != 2:

            count = 0
            print_text("Invalid Choice! Please try again!")

            return


#Login Page:

def Register_and_Login():

    print_text("In order to book a ticket in Easy2BookNFly.com, you need to follow the procedure carefully") 
    print_text("We shall be guiding you to register yourself in our website. Follow the rules as instructed below:")

    while True:

        Name = input(print_text("Enter your name:"))

        while True:

            Create_Username=input(print_text("Enter your username (format: <username>@booknfly.com):"))

            if "@booknfly.com" not in Create_Username:

                print_text("Please enter a valid user name (as per the format mentioned within the parentheses!)")

            else:

                break

        break

    print_text("Setup a password for your account :")
    Create_Password = input(print_text("Enter your desired password to be set for your account:"))      
    print_text("Now we will be redirecting you to our website's login page :)")
    print_text("Enter the login credentials as requested below:")

    while True:

        Username = input(print_text("Enter your username:"))
        Password = input(print_text("Enter your password:"))
 
        if Username != Create_Username:

            print_text("Invalid username, please try again !!")

        elif Password != Create_Password:

                print_text("Incorrect password, please try again!")
        
        else:

            print_text("Hurray!! You have successfully logged in to Easy2BookNFly website!!")
            break

    print_text("Now you can book your airline ticket.")

    Choose_Region()

Register_and_Login()


def Modifications():

    choice=input(print_text("Do you wish to perform any changes/modifications in your flight ticket ? (yes/no):"))

    while True:

        if choice.lower() == "yes":

            print_text("Choose one of the following changes that you wish to perform:")
            print_text("1.Modify data within a specific row/column")
            print_text("2.Add/Delete an entire row/coloumn")

            while True:

                try:

                    inner_choice = int(input(print_text("Enter your choice from above menu (1/2):")))

                    if inner_choice == 1:

                        Update()

                        break

                        #connection_string.close()

                    elif inner_choice == 2:

                        Delete()

                        break

                        #connection_string.close()

                except ValueError:

                    print_text("Expected integer data type!")

                    break
                break
            break
        
            

        elif choice.lower() == "no":

             print_text("No worries, the passengers' details are safe. None of them have been modified yet :)")
             print_text("Thank you!! Your name has been successfully registered!.")

             Payment()
             
             break
    
            
        

        else:
            
            print_text("Invalid Choice! Please try again!")

            return

Modifications()

print_text("Thank you!! Your airline ticket has been successfully booked!")

print_text("Wishing you a very happy journey!! :))")

