import calendar

year = int(input("Enter year: \n "))
month = int(input("Enter month: \n "))
mycalendar = calendar.month(year,month)
print(mycalendar)