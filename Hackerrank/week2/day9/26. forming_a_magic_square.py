""" 
Continuing the problem from the previous day 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def calculate_cost(s, magic_square):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(s[i][j] - magic_square[i][j])

    return cost

def formingMagicSquare(s):
    magic_square_1 = [
        [8, 3, 4],
        [1, 5, 9],
        [6, 7, 2]
    ]
    magic_square_2 = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]
    magic_square_3 = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
    magic_square_4 = [
        [6, 1, 8],
        [7, 5, 3],
        [2, 9, 4]
    ]
    magic_square_5 = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    magic_square_6 = [
        [4, 3, 8],
        [9, 5, 1],
        [2, 7, 6]
    ]
    magic_square_7 = [
        [2, 9, 4],
        [7, 5, 3],
        [6, 1, 8]
    ]
    magic_square_8 = [
        [6, 7, 2],
        [1, 5, 9],
        [8, 3, 4]
    ]
    
    magic_squares = [
        magic_square_1,
        magic_square_2,
        magic_square_3,
        magic_square_4,
        magic_square_5,
        magic_square_6,
        magic_square_7,
        magic_square_8
    ]

    cost = float('inf')
    for magic_square in magic_squares:
        cost = min(cost, calculate_cost(s, magic_square))
    
    return cost


if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(str(result) + '\n')

