year = int(input('enter a number'))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is leapyear".format(year))
        else:
            print("{0} is a leapyear".format(year))
    else:
        print("{0} is a leapyear".format(year))
else:
    print("{0} is not a leapyear".format(year))
