#A progam that computes the day one was born.
#1 Importing the datetime module which is to be used in the precceeding statements
import datetime
#2 Getting values from the user
Date_of_Birth=int(input("Pease Enter Your Date of Birth:\n "))
Month_of_Birth=int(input("Please Enter Your Month of Birth:\n "))
Age=int(input("Please Enter Your Age:\n "))
#3 Computing the current date
DateNow=datetime.datetime.now()
DaysPerYear=365
DaysLived=DaysPerYear*Age
#4 Converting the days lived into DD/MM/YY format
DaysLived_in_Timedelta= datetime.timedelta(days=DaysLived)
#5 Calculating the year of birth
Year_of_Birth=DateNow-DaysLived_in_Timedelta
#6 Converting the year of birth from string data type to integer data type
RealYear_of_Birth=int(Year_of_Birth.strftime("%Y"))
#7 Calculating the actual date of birth in calender format(day/date/month/year)
ActualDate_of_Birth=datetime.date(RealYear_of_Birth,Month_of_Birth,Date_of_Birth)
#8 Extracting the day the user was born and printing it out
print("You Were Born On a ",ActualDate_of_Birth.strftime("%A"))


