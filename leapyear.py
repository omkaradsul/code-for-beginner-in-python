import calendar

year = int(input("enter year:"))
if year is calendar.isleap(year):
    print(" {year}, year is leap year")
else:
    print('year is not leap year')