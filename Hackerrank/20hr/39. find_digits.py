"""
An integer d is a divisor of an integer n if the remainder of n / d = 0.

Given an integer, for each digit that makes up the integer determine whether it is a divisor. 
Count the number of divisors occurring within the integer.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here

    # Making the digits of the number into a list so it can be iterated
    number = []

    text = str(n)
    for char in text:
        number.append(int(char))

    # An easier one liner way is to do this
    # number = [int(char) for char in str(n)]

    count = 0
    for digit in number:
        # The condition of != 0 because we get ZeroDivisonError if there is a digit 0 in a number
        if digit != 0 and n % digit == 0:
            count += 1
    
    return count

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(str(result) + '\n')
