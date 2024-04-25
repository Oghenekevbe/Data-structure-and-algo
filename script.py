def is_leap(year):
    leap = False

    # The year can be evenly divided by 4
    if year % 4 == 0:

        # The year can be evenly divided by 100, it is NOT a leap year, unless the year is also evenly divisible by 400
        if year % 100 == 0 and year % 400 == 0:
            leap = True

        # so it doesn't return other values evenly divisible by 4 but not evenly divisble by 100 and 400 as False
        elif year % 100 != 0 and year % 400 != 0:
            leap = True

    return leap


year = int(input())
print(is_leap(year))
