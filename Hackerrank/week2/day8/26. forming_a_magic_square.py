"""
This is not a complete solution. The complete solution is in the next day. 
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

def formingMagicSquare(s):
    magic_number = 9
    duplicates = []
    missing = []
    
    for number in range(1, magic_number+1):
        count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if number == s[i][j]:
                    count += 1
        
        if count > 1 and number not in duplicates:
            duplicates.append(number)
        if count == 0:
            missing.append(number)
    
    cost = 0
    for duplicate_number, missing_number in zip(duplicates, missing):
        cost += abs(duplicate_number - missing_number)
        number_changed = False
        
        for i in range(0, 3):
            for j in range(0, 3):
                if duplicate_number == s[i][j]:
                    s[i][j] = missing_number
                    number_changed = True
                    break
            if number_changed == True:
                break

    print(s)
    
    return cost


if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(str(result) + '\n')


""" 
I was successful in making every number in the square identical by replacing the duplicates with the missing numbers.
But in order to make the square a magic square. Every column, row and diagonal needs to add upto the magic number 
and then calculate the minimal cost.

I looked at the forum. Out of all the problems, I find the solution to this problem to be the biggest cop out. 
I mean seriously??? Having predefined set of magic squares and then calculating the minimal cost from that. 
I expected a better solution :((

"""