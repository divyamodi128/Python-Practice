def checkLeapYear(year):
    return (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)

print checkLeapYear(int(raw_input()))