"""
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, 
discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest 
stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. 
When all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    sticks_cut = []
    non_zero = [num for num in arr if num > 0]
    while len(non_zero) != 0:
        minimum = min(non_zero)
        non_zero = [num - minimum for num in non_zero]
        sticks_cut.append(len(non_zero))
        non_zero = [num for num in non_zero if num > 0]

    return sticks_cut    

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))
    print('\n')

    # arr = [9, 2, 1, 5, 5]
    # print(cutTheSticks(arr))
