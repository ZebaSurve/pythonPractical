year = int(input("enter the year:\n"))
print(year)

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is not a leap year.")