#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    index = n - 1
    for i in range(n):
        string = ""
        for j in range(n):
            if j < index:
                string += " "
            else:
                string += "#"
        print(string)
        index -= 1

staircase(4)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
