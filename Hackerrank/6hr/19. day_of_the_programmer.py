"""
Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer 
(the 256th day of the year) during a year in the inclusive range from 1700 to 2700.

From 1700 to 1917, Russia's official calendar was the Julian calendar; since 1919 they used the Gregorian calendar system. 
The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. 
This means that in 1918, February 14th was the 32nd day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a leap year, 
and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, 
leap years are either of the following:

Divisible by 400.
Divisible by 4 and not divisible by 100. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    day_of_programmer = 256

    months_in_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # If there is any year before 1918 which is a leap year, simply add one more day to the total days of feb
    if year < 1918:
        if year % 4 == 0:
            days = months_in_year[1]
            days += 1
            months_in_year[1] = days
    # If the year is 1918 then subtract 13 days cause of the calender shift the date went from 31st january to 14th Februrary
    elif year == 1918:
        days = months_in_year[1]
        days -= 13
        months_in_year[1] = days
    # If the year is after 1918, there were two ways to calculate the leap year 
    # 1. If it is divisible be 400
    # 2. If it is divisible by 4 and not by 100
    elif year > 1918:   
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = months_in_year[1]
            days += 1
            months_in_year[1] = days
    
    days_sum = 0
    month = 0
    
    for days in months_in_year:
        # 256 - 0
        # 256 - 31
        # 256 - (31 + 28) ... we can adding the days in a month till the difference is smaller than the days in a month
        # which would be the days left in a month
        days_left = day_of_programmer - days_sum
        if days_left > days:
            days_sum += days
            month += 1

    # zfill adds 0 before the singluar digit of a month like 9 to 09
    date = ""
    date += str(days_left).zfill(2) + "."
    # Adding 1 because we did not account for the current month... as we stopped counting before we reached this month
    date += str(month + 1).zfill(2) + "."
    date += str(year)

    return date

    

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')

