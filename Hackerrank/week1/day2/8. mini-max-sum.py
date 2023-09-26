'''
Problem Statement:
Given five positive integers, find the minimum and maximum values that can be calculated 
by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    min_sum = 0
    max_sum = 0
    
    # Adding the first four smallest numbers which s the min_sum
    min_arr = arr[:4]
    for i in range(len(min_arr)):
        min_sum += min_arr[i]

    # Adding the last four largest numbers which is the max_sum
    max_arr = arr[-4:]
    for i in range(len(max_arr)):
        max_sum += max_arr[i]

    print(f'{min_sum} {max_sum}')
    

if __name__ == '__main__':

    arr = [18, 5, 9, 2, 1]

    miniMaxSum(arr)
