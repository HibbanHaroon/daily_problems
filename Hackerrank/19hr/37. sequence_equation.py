"""
Given a sequence of  integers, p(1), p(2), ... , p(n) where each element is distinct and satisfies 1 <= p(x) <= n. 
For each x where 1 <= x <= n, that is x increments from 1 to n, find any integer y such that p(p(y)) = x and 
keep a history of the values of y in a return array.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    n = len(p)
    y = []

    for i in range(1, n + 1):
        index = p.index(i) + 1
        y.append(p.index(index) + 1)
    
    return y

if __name__ == '__main__':

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str, result)))
    print('\n')
