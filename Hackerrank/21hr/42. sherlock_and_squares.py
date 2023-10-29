"""
Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, 
inclusive of the endpoints. Sherlock must determine the number of square integers within that range.
"""
#!/bin/python3

import math
import os
import random
import re
import sys
import math

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    lower = math.ceil(math.sqrt(a))
    upper = math.floor(math.sqrt(b))

    # If the bounds were 24 and 50
    # then sqrt(24) would be 4.89, and sqrt(50) would be 7.07
    # 4.89 means that 5's square lies in the range and 4's does not, so we ceil it
    # 7.07 means that 7's square definitely lies in the range so we floor it
    # then lower would be 5 and upper would be 7 

    # 5, 6, 7 are the numbers that have their squares between the ranges 24 and 50
    # The difference of lower and upper plus 1 would be the number of squares between the range
    # If we subtract 7 - 5, it would give 2, we missed one of the numbers when subtracting, so simply add 1

    return (upper - lower) + 1

# First Try
# def squares(a, b):
#     count_squares = 0

#     # Firstly, finding square root of a number
#     # If this sqrt and when applied ceiling function on it is same
#     # means that the number is a square
#     for number in range(a, b + 1):
#         num = math.sqrt(number)
#         if num == math.ceil(num):
#             count_squares += 1

#     return count_squares


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        print(str(result) + '\n')
