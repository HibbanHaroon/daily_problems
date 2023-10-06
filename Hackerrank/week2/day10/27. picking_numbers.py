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

all_subarrays = []

def get_subarrays(arr, k, start=0, current=[]):
    if k == 0:
        if len(current) >= 2:
            all_subarrays.append(current.copy())
        return all_subarrays
    for i in range(start, len(arr)):
        current.append(arr[i])
        get_subarrays(arr, k - 1, i + 1, current)
        current.pop()

def generate_subarrays_with_decreasing_lengths(arr):
    max_length = len(arr)
    for subarray_length in range(max_length, 0, -1):
        get_subarrays(arr, subarray_length)

def pickingNumbers(a):
    generate_subarrays_with_decreasing_lengths(a)
    longest_sequence = 0
    for subarray in all_subarrays:
        longest_sequence_found = True
        n = len(subarray) - 1
        index = 0
        while index <= n - 1:
            if not abs(subarray[index] - subarray[index + 1]) <= 1:
                longest_sequence_found = False
                break
            index += 1
        
        if longest_sequence_found == True:
            longest_sequence = len(subarray)
            return longest_sequence

    return longest_sequence


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')


"""
It will give the correct result. The logic is correct. However, the time complexity is through the roof (2 ^ n). 
Gonna look at the forum for the correct approach tomorrow. 
"""