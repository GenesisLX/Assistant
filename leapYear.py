import datetime

def leap_year_definition():
    year = datetime.date.today().year
    if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(str(year) + " - високосный.")
    else:
        print(str(year) + " - невисокосный.")


