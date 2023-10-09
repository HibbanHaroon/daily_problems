"""
Given an array of bird sightings where every element represents a bird type id, 
determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, 
return the smallest of their ids. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):

    # Finding the number of sightings of each bird or the number of occurences of each bird
    sightings = {}
    for bird_id in arr:
        # If the bird is already sighted simply increment the count otherwise assign it 1 since it our first sighting
        if bird_id in sightings:
            count = sightings[bird_id]
            count += 1
            sightings[bird_id] = count
        else:
            sightings[bird_id] = 1

    max_bird_id = 0
    maximum = 0
    count = 0

    # Finding the bird which has the most sightings
    for bird_id in sightings:
        if count == 0:
            maximum = sightings[bird_id]

        if maximum < sightings[bird_id]:
            maximum = sightings[bird_id]
            max_bird_id = bird_id
        count += 1

    # If there are other birds who also have the maximum sightings. Return the bird with the smallest bird id or bird type
    # Assuming that the bird id we found above is the smallest bird id
    lowest_bird_id = max_bird_id

    # Comparing this lowest bird id with other ids who also have the maximum sightings
    for bird_id in sightings:
        if maximum == sightings[bird_id]:
            # If we found another bird id which is smaller, then make it the lowest bird id
            if lowest_bird_id > bird_id:
                lowest_bird_id = bird_id

    return lowest_bird_id

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')
