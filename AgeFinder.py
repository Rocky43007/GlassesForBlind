# Created by GeeksForGeeks, modified by Arnab Chakraborty 
# Copyright Arnab Chakraborty 2020
# -------------------------------------------------------
# Using datetime, we can import date to calculate age in years.  
from datetime import date 
# Using the data gotten from __init__.py, 
# We can use that data to find the age of the user.
import pickle

# Opening the file with Pickle, we can take the data and remove the time and the dashes.
# For example, the saved data comes as 1999-05-01 00:00:00.
with open('birthday.native', 'rb') as f:
    x = pickle.load(f)
    # After bringing the data into the code, we can strip the 00:00:00 and the - 
    # from the date.
    a = x.strip("00:00:00")
    d = a.split("-")
# Here, we print the date only,
print ("Original list is : " + str(d)) 

# Which we then save as an integer instead of the string+list is which it is saved as.
for i in range(0, len(d)): 
    d[i] = int(d[i]) 

  
print ("Modified list is : " + str(d))
# Then we split the 3 integers into year, month and day for us to find the age. 
year, month, day = d
print (year, month, day)

# This code takes the variables year, month and day, and gives us the age using maths.
def calculateAge(born):
    # This takes local time and finds the date. 
    today = date.today() 
    try:
        # makes birthday variable replace the year variable defined before as the year 
        # the user is in.  
        birthday = born.replace(year = today.year) 
  
    # raised when birth date is February 29 
    # and the current year is not a leap year 
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
    
    # This checks if the birthday is greater than the birth year, 
    # and then either subtracts the birth year from the current year and subtracts an extra 
    # year.
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year 
          
# Driver code
# This code is the command, using the variables which we got from
# the saved file. 
age = calculateAge(date(year, month, day))
print (age)

#Testing Purposes Only.
meter = 100
if age in range(20,29):
    print ('Steps = 1.35 m/s')
    steps = round(meter/1.35)
    print (steps)

elif age in range(30,39):
    print ('Steps = 1.385 m/s')
    steps = round(meter/1.35)
    print (steps)

stepstxt = "and the object is %s steps away" % steps
print (stepstxt)