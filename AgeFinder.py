# Python3 code to  calculate age in years 
from datetime import date 
import pickle
import datefinder

with open('birthday.native', 'rb') as f:
    x = pickle.load(f)
    a = x.strip("00:00:00")
    d = a.split("-")

print ("Original list is : " + str(d)) 

for i in range(0, len(d)): 
    d[i] = int(d[i]) 

  
print ("Modified list is : " + str(d)) 
year, month, day = d
print (year, month, day)
def calculateAge(born): 
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year) 
  
    # raised when birth date is February 29 
    # and the current year is not a leap year 
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
  
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year 
          
# Driver code 
age = calculateAge(date(year, month, day))
print (age) 
meter = 100

if age in range(20,29):
    print ('Steps = 1.35 m/s')
    steps = meter/1.35
    print (steps)

elif age in range(30,39):
    print ('Steps = 1.35 m/s')
    steps = meter/1.35
    print (steps)

stepstxt = "and the object is %s steps away" % steps
print (stepstxt)