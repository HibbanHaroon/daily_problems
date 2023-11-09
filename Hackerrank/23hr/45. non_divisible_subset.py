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
from itertools import combinations

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
def nonDivisibleSubset(k, s):
    largest_subset = 2

    arrays = []
    for i in range(2, len(s) + 1):
        arrays.append(list(combinations(s, i)))

    print(list(arrays))

    for arr in list(arrays):
        for subset in arr:
            tuples = combinations(subset, 2)
            is_largest_subset = True
        
            for tup in list(tuples):
                if (tup[0] + tup[1]) % k == 0:
                    is_largest_subset = False
            
            if is_largest_subset == True:
                largest_subset = len(subset)
    
    return largest_subset

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

