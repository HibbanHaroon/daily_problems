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
from collections import Counter

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

# Detailed Explanation at the end
def nonDivisibleSubset(k, s):
    # An array to store the frequencies of remainders when divided by k
    # The following code will make a list where k is 5 as [0, 0, 0, 0, 0]
    frequency_of_remainder = [0] * k

    # Count the frequencies of each remainder
    for element in s:
        frequency_of_remainder[element % k] += 1

    # In the case of even k, if in the list there is more than 1 number which results in the remainder k // 2, then count only 1
    # Limiting the remainder to 1 because adding two numbers with remainder k // 2 would be divisible by k. Same goes for remainder 0.
    if k % 2 == 0:
        frequency_of_remainder[k//2] = min(frequency_of_remainder[k//2], 1)
    
    count = 0

    # Same in the case of remainder 0, if there is more than 1 number which results in remainder 0, then count only 1
    count += min(frequency_of_remainder[0], 1)

    # Iterate up to k//2 (inclusive) to avoid duplicates
    for i in range(1, (k//2) + 1):
        count += max(frequency_of_remainder[i], frequency_of_remainder[k - i])

    return count

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(str(result) + '\n')

    # k = 3
    # s = [1, 7, 2, 4]
    # print(nonDivisibleSubset(k, s))

# Explanation:
# For example s = [1, 2, 3, 4, 5]
# Step 1: Create a frequency list of all the remainders taken by dividing the numbers in the list with k. 
# Step 2: In the case of even k, if in the list there is more than 1 number which results in the remainder k // 2, then count only 1
# Limiting the remainder to 1 because adding two numbers with remainder k // 2 would be divisible by k. Same goes for remainder 0.
# Step 3: If in the list there more than 1 number which results in the remainder 0, then count only 1.
# Step 4: Iterate from 1 to (k // 2 + 1), as 0 has been counted, so starting from 1. k // 2 is not counted yet, so including it by adding 1
# The reason for running the loop till k // 2 is that to avoid the counting of remainders we have already considered.
# As, if the remainder is 1, it's k - i where k is 5 and i is 1 for example would be 4. We are addressing the remainder 4 with 1.
# As, if the remainder is 2, it's k - i where k is 5 and i is 2 for example would be 3. We are addressing the remainder 3 with 2.
# So, there is no need to do traversing after k // 2. 
# Step 5: Choose the max of frequency of remainder i and k - i. The max would allow that we don't overcount. 
# If frequency of 1 and 4 in the case of k = 5 are 3 and 2. By choosing the max 3, 
# we are ensuring that the numbers in the list s, when added up, and we get these remainders 1 and 4 when divided by k, are all accounted for. 