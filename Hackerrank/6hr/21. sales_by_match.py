"""
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    socks = {}
    for sock in ar:
        if sock not in socks:
            socks[sock] = 1
        else:
            count = socks[sock]
            count += 1
            socks[sock] = count
    
    pairs = 0

    # For each sock, we are counting pairs. 
    # If the count is 7, divided by 2 with floor division operator would result in 3 
    for sock in socks:
        count = socks[sock]
        pairs += count // 2

    return pairs

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')
