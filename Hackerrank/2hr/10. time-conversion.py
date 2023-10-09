'''
Problem Statement:
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Splitting the time in a list having hh, mm, ssPM/AM as elements
    time = s.split(":")
    
    # Extracting AM or PM from the last element which is seconds
    am_or_pm = time[2][2:4]

    # Removing the AM or PM from the seconds
    time[2] = time[2][0:2]

    hour = int(time[0])
    
    # If hour is between 1 and 11 in PM just add 12 that will make them 13 - 23
    if hour != 12 and am_or_pm.upper() == "PM":
        hour += 12
        time[0] = str(hour)
    
    # If hour is 12 and it's AM then just make it 0 with a leading zero.
    if hour == 12 and am_or_pm.upper() == "AM":
        hour = 0 
        time[0] = str(hour).zfill(2)
    
    return time[0] + ":" + time[1] + ":" + time[2]


if __name__ == '__main__':

    s = "12:05:45AM"

    result = timeConversion(s)

    print(result)
