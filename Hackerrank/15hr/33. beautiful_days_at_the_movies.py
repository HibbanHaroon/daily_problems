"""
Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. 
For instance, given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 99.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days, [i ... j] and a number k, determine the number of days in the range that are beautiful. Beautiful numbers are 
defined as numbers where |i-reverse(i)| is evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. 
Return the number of beautiful days in the range. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    beautiful_days = []
    for day in range(i, j+1):
        day_string = str(day)
        
        # Making the characters into a list such as "123" -> ["1", "2", "3"]
        day_characters_list = []
        for characters in day_string:
            day_characters_list.append(characters)
        
        # Reversing the list such as ["1", "2", "3"] -> ["3", "2", "1"]
        # Then joining the list such as ["3", "2", "1"] -> "321"
        day_characters_list.reverse()
        reverse = day_characters_list
        reverse = "".join(reverse)
        reverse = int(reverse)
        
        if abs(reverse - day) % k == 0:
            beautiful_days.append(day)

    return len(beautiful_days)
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print(str(result) + '\n')

"""
I looked at the forum and found that there is a better way to reverse a number
int(str(num)[::-1]) 

Explanation:
1. The first colon means that all the elements from the beginning to the end will be travered.
2. The second colon is used to specify the step. -1 Indicates that you will traverse the string in reverse order.

"""
