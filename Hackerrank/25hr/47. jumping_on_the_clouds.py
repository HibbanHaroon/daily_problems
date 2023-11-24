""" 
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads 
and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of 
the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it 
will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    jumps = 0
    n = 0
    
    # First checking if I can jump on n + 2, then go for it, otherwise jump n + 1. 
    # Also checking if n + 2 or n + 1 exists. And If we have reached len - 1, then we stop.
    while n != len(c) - 1:
        if n + 2 < len(c) and c[n + 2] == 0:
            n += 2
            jumps += 1
        elif n + 1 < len(c) and c[n + 1] == 0:
            n += 1
            jumps += 1
    
    return jumps
    
if __name__ == '__main__':

    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))

    # n = 7
    # c = [0, 0, 1, 0, 0, 1, 0]

    result = jumpingOnClouds(c)

    print(str(result) + '\n')