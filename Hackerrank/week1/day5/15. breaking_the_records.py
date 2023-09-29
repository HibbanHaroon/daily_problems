"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # min count and max count is the number of times minimum and maximum changes respectively.
    min_count = 0
    max_count = 0

    # Finding the minimum and maximum score
    minimum = scores[0]
    maximum = scores[0]

    for score in scores:
        # Incrementing the max_count if the maximum score changes. 
        if maximum < score:
            maximum = score
            max_count += 1

        # Incrementing the min_count if the minimum score changes. 
        elif minimum > score:
            minimum = score
            min_count += 1
    
    return [max_count, min_count]


if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')
