""" 
A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights, 
and the characters have a maximum height they can jump. There is a magic potion they can take that will increase 
their maximum jump height by 1 unit for each dose. How many doses of the potion must the character take to be able 
to jump all of the hurdles. If the character can already clear all of the hurdles, return 0.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    maximum = max(height)
    diff = maximum - k
    if diff > 0:
        return diff
    else:
        return 0

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(str(result) + '\n')
