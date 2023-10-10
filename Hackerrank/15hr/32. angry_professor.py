"""
A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, 
the professor decides to cancel class if fewer than some number of students are present when class starts. 
Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivedLate > 0).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    number_of_students_on_time = 0
    for arrivalTime in a:
        if arrivalTime <= 0:
            number_of_students_on_time += 1
    
    if number_of_students_on_time >= k:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
