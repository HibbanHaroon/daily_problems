"""
A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be 
thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i = 0
    e = 100

    while True:
        i = (i + k) % n
        if c[i] == 0:
            e = e - 1
        elif c[i] == 1:
            e = e - 1 - 2

        if i == 0:
            break
    
    return e

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(str(result) + '\n')

