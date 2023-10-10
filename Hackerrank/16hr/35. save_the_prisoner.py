"""
A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide 
the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. 
Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been 
distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. 
Determine the chair number occupied by the prisoner who will receive that candy. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    
    # Firstly, finding the multiple of n before we reach m
    product = next_product = 0
    count = 0
    while next_product <= m:
        product = n * count
        count += 1
        next_product = n * count
    
    # Subtracting this multiple from m
    diff = abs(product - m)
    chair = (s + diff) - 1

    # Since the chairs start from 1, if there is a zero which means it is the last chair. Give this candy to the last chair
    if chair == 0:
        chair = m
    
    # If the value is greater than n then simply take mod.
    if chair % n != 0:
        chair = chair % n

    return chair
    

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        print(str(result) + '\n')
        
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])

    # s = int(first_multiple_input[2])

    # result = saveThePrisoner(n, m, s)

    # print(str(result) + '\n')

"""
The problem is not all the test cases are being passed due to time complexity. 
"""