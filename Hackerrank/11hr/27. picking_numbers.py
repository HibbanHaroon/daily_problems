"""
Given an array of integers, find the longest subarray where the absolute difference between any two elements 
is less than or equal to 1  
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    frequencies = dict()

    for num in a:
        if num not in frequencies:
            frequencies[num] = 1
        else:
            count = frequencies[num]
            frequencies[num] = count + 1

    maximum = 0
    for freq in frequencies:
        count = frequencies[freq]
        if freq + 1 in frequencies:
            count += frequencies[freq + 1]
        maximum = max(maximum, count)        

    return maximum

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')

"""
I'm honestly speechless how good of a solution this is compared to my previous solution where I solved the problem through
recursion. Thanks to the forum for inspiration.
"""