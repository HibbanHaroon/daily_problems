"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # The segments that satisfies the day condition are stored in day_segments 
    # i.e., the sum of the continuous numbers in the list should add up to the days
    day_segments = []
    length = len(s)

    # We iterate through every number in the list, and add that number to the subsequent number 
    # until sum of the numbers is less than d or we have hit the end of the list, then we check for the next the number
    
    # For example if the list = [2, 2, 1, 3, 4], d = 4 and m = 4
    # We take 2, add it to the next number which is 2 then check if the sum is less than 4, it is not so the while loop breaks, 
    # so then we check if the sum equals to d, in this case it does, so we add this continuous segment 2 to the day_segments list 
    # and then start finding another segment from the next number in this list which is again 2

    # Iterating for every number in the list
    for i in range(length):
        numbers_sum = 0
        segment = []
        index = i
        
        # Checking if the sum is less than d or if we have reached the end of the list
        while numbers_sum < d and index < length:
            current_num = s[index]
            numbers_sum += current_num
            segment.append(current_num)
            index += 1

        # If we have found the continuous segment and the sum of the numbers in the segment is equal to d
        # then add it to the day_segments since it satisfies our condition
        if len(segment) > 0 and numbers_sum == d:
            day_segments.append(segment)
    
    # The segments that already satisfied the day condition are then checked if they also satisfy the month condition 
    # i.e, the length of any day segment should be equal to month
    month_segments = []
    for segment in day_segments:
        if len(segment) == m:
            month_segments.append(segment)

    # Returning the number of continuous segments we have found that satisfies both of the conditions
    return len(month_segments)

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')
