#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    cummulative_sum_of_likes = 0
    shared = 5
    for day in range(0, n):
        like = shared // 2
        cummulative_sum_of_likes += like
        shared = like * 3

    return cummulative_sum_of_likes


if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)

    print(str(result) + '\n')
