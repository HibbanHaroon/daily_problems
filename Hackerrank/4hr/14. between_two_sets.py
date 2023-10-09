"""
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # The numbers in the list a are the factors of some number(s). 
    # So, the largest number in list a will be smaller or equal to the number(s) X
    # For example: a = [2, 3, 6]. the number(s) X will be greater than the numbers in list a as they are the factors of the number(s) X
    # We can use this largest number as the starting point.

    largest = a[0]
    for num in a:
        if largest < num:
            largest = num
    
    starting_point = largest

    # The number(s) X are the factors of the numbers in in the list b.
    # So, the number(s) X will be smaller than the smallest number in the list b as number(s) X are the factor(s) of the numbers in list b.
    # For example: X are 6, and 12, b = [24, 36]. the number(s) X will be smaller than the numbers in list b.
    # We can use this smallest number as the ending point.
    smallest = b[0]
    for num in b:
        if smallest > num:
            smallest = num

    # Adding one to make the number inclusive
    ending_point = smallest + 1

    list_of_X_numbers = []

    # Finding the number(s) X
    for num in range(starting_point, ending_point):
        all_factors_in_A = True
        i = 0

        # Checking if all the numbers in list A are factors of the current number we are iterating for.
        while all_factors_in_A == True and i < len(a):
            factor_in_A = a[i]
            if num % factor_in_A == 0:
                all_factors_in_A = True
                i += 1
            else:
                all_factors_in_A = False
        
        # If all the numbers in A are factors, now check whether the current number is a factor for all numbers in list b.
        if all_factors_in_A == True:
            is_num_factor_of_B_numbers = True
            j = 0
            while is_num_factor_of_B_numbers == True and j < len(b):
                factor_in_B = b[j]
                if factor_in_B % num == 0:
                    is_num_factor_of_B_numbers = True
                    j += 1
                else:
                    is_num_factor_of_B_numbers = False
            
            # If the current number is a factor of all the numbers in list b, then append it to the list
            if is_num_factor_of_B_numbers == True:
                list_of_X_numbers.append(num)

    # Return the number of X numbers found between the two lists
    return len(list_of_X_numbers)
            

if __name__ == '__main__':

    # First input is the length of list A and list B separated by a space
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    # Second input is the n numbers in the list A separated by spaces
    arr = list(map(int, input().rstrip().split()))

    # Third input is the m numbers in the list B separated by spaces
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')

    