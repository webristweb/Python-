year = int(input("Enter a Year"))

if (year % 400 == 0) and (year % 100 == 0):
    print(year, "Is a leap year")

elif(year & 4 == 0) and (year % 100 != 0):
    print(year, "Is a leap year")
else:
    print(year, "Is not a leap year")
