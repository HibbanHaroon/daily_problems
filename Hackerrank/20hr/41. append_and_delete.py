"""
You have two strings of lowercase English letters. You can perform two types of operations on the first string:

1. Append a lowercase English letter to the end of the string.
2. Delete the last character of the string. Performing this operation on an empty string results in an empty string.
Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k 
of the above operations on s. If it's possible, print Yes. Otherwise, print No.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here

    if s == t:
        return "Yes"
    else:
        same = 0
        for elementS, elementT in zip(s, t):
            if elementS == elementT:
                same += 1
            else:
                break
        
        diffS = len(s) - same
        diffT = len(t) - same

        # If there are no different in S such as s = a, b and t = a, b, c, d
        if diffS == 0:
            if diffT % 2 == 0:
                return "Yes"
            else:
                return "No"

        # Otherwise if there are some different in S such as s = a, b, c, d and t = a, b
        if diffS + diffT <= k:
            return "Yes"
        else:
            return "No"

if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result + '\n')
