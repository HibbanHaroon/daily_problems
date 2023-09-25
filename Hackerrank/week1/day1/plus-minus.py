#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total_numbers = len(arr)
    no_of_positives = 0
    no_of_negatives = 0
    no_of_zeroes = 0
    
    for num in arr:
        if num == 0:
            no_of_zeroes += 1
        elif num > 0:
            no_of_positives += 1
        elif num < 0:
            no_of_negatives += 1

    positive_ratio = no_of_positives/total_numbers
    negative_ratio = no_of_negatives/total_numbers
    zero_ratio = no_of_zeroes/total_numbers
        
    print(f'{positive_ratio:.6f}')
    print(f'{negative_ratio:.6f}')
    print(f'{zero_ratio:.6f}')



if __name__ == '__main__':

    arr = [1, 1, 0, -1, -1]

    plusMinus(arr)
