import datetime
date = int(input("Enter Your Birth Date : "))
month = int(input("Enter Your Birth Month : "))
year = int(input("Enter Your Birth Year : "))

month1 = {1:31 ,2:28 ,3:31 ,4:30 ,5:31 ,6:30 ,7:31 ,8:31 ,9:30 ,10:31 ,11:30 ,12:31}
month2 = {1:31 ,2:59 ,3:90 ,4:120 ,5:151 ,6:181 ,7:212 ,8:243 ,9:273 ,10:304 ,11:334 ,12:365}
months = {"Jan":1 ,"Feb":2 ,"Mar":3 ,"Apr":4 ,"May":5 ,"June":6 ,"Jul":7 ,"Aug":8 ,"Sep":9 ,"Oct":10 ,"Nov":11 ,"Dec":12}

rawtime = datetime.datetime.now()
currMonth = rawtime.strftime("%B")  # months
currDay = rawtime.strftime("%d")  # days
currYear = rawtime.strftime("%Y")  # years

currDay = int(currDay)
currYear = int(currYear)

yearDays = (currYear - year)*365
monthDays = month2[month-1]
lastDays = month1[month-1] - date

allDays = yearDays + monthDays + lastDays + currDay 
print(f"The Day of Alive is {allDays}")