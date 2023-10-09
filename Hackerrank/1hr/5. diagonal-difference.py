#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    m = len(arr[0])
    start_index = 0
    last_index = m-1
    sum1 = 0
    sum2 = 0
    
    for ar in arr:
        sum1 += ar[start_index]
        print(sum1)
        start_index += 1
    
    for ar in arr:
        sum2 += ar[last_index]
        print(sum2)
        last_index -= 1
    
    return abs(sum1 - sum2)



arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

result = diagonalDifference(arr)

print(str(result) + '\n')
