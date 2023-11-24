"""
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    count = 0

    # Counting the number of a's in s here. For instance, there are 2 a's in 'aab'
    for character in s:
        if character == 'a':
            count += 1
    
    # If the length is 3, and n is 10. We will find the multiple of length before we reach 10 which is 9 in this case.
    # So, 3 * 3 is 9, Hence, there would be 3 iterations, so we simply multiple the count for one iteration with 3.
    iterations = n // len(s)
    count = count * iterations

    # We have counted till 9, we have to account for the remaining, so if n is 10, 10 % 3 would be 1
    # We simply count any remaining a's
    for i in range(n % len(s)):
        if s[i] == 'a':
            count += 1
    
    return count


if __name__ == '__main__':

    s = input()

    n = int(input().strip())
    
    # s = 'aab'
    # n = 882787

    result = repeatedString(s, n)

    print(str(result) + '\n')
 