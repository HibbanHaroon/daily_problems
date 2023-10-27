"""
John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves
 the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, 
 Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times 
 then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the values of the elements at the given indices. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here

    n = len(a)

    # Starting the pointer from last and moving it k steps back
    pointer = n
    pointer -= k
    pointer %= n
    
    q = []

    # To find the element at index 'query', just move the pointer forward 'query' steps.
    for query in queries:
        i = query + pointer
        i %= n

        q.append(a[i])
    
    return q

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print('\n'.join(map(str, result)))
    print('\n')