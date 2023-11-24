"""
Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    dic = {}
    for num in arr:
        if num in dic:
            dic[num] = dic.get(num) + 1
        else:
            dic[num] = 1
    
    sumOfOccurrences = sum(dic.values())
    maximumOfOccurrences = max(dic.values())

    return sumOfOccurrences - maximumOfOccurrences

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    arr = [3, 3, 2, 1, 3]

    result = equalizeArray(arr)

    print(str(result) + '\n')

    # fptr.close()
