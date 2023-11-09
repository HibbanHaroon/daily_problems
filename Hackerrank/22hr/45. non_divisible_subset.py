"""
Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in  S`
is not evenly divisible by k.

"""

# The code is not meeting all the test cases and I understand the problem.
# The problem is basically after adding the numbers in the list, there might be two numbers(the number being currently entered
# and the one from before) that when adding are still divisble even though the current numbers being added are not divisible.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    non_divisible = []
    
    for i, _ in enumerate(s):
        for j, _ in enumerate(s, i + 1):
            if j < len(s): # This condition will ensure that j doesn't go out of range
                if (s[i] + s[j]) % k != 0:
                    non_divisible.extend([s[i], s[j]]) #extends add multiple elements to a list but it takes a list, set or tuple as arguments.
    
    non_divisible = set(non_divisible)

    return len(non_divisible)

if __name__ == '__main__':

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # s = list(map(int, input().rstrip().split()))

    # result = nonDivisibleSubset(k, s)

    # print(str(result) + '\n')

    k = 3
    s = [1, 7, 2, 4]
    print(nonDivisibleSubset(k, s))
