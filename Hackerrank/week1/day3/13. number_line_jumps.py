"""
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

Complete the function kangaroo in the editor below.

kangaroo has the following parameter(s):

int x1, int v1: starting position and jump distance for kangaroo 1
int x2, int v2: starting position and jump distance for kangaroo 2

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if not ((x1 >= 0 and x1 <= 10000) or (x2 >= 0 and x2 <= 10000)):
        return "NO"
    elif not x2 > x1:
        return "NO"
    elif not ((v1 >= 1 and v1 <= 10000) or (v2 >= 1 and v2 <= 10000)):
        return "NO"
    else:
        for i in range(10000):
            jump1 = x1 + v1
            jump2 = x2 + v2
            
            if jump1 == jump2:
                return "YES"
            
            x1 = jump1
            x2 = jump2
        
        return "NO"


if __name__ == '__main__':

    # Enter the numbers separated by spaces e.g., 0 3 4 2
    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')
