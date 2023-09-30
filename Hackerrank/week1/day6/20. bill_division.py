""" 
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. 
Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    actual_bill = 0
    for item in range(0, len(bill)):
        # If Anna hasn't ate this dish then don't add it to the bill
        if item != k:
            actual_bill += bill[item]
    
    actual_bill_per_person = actual_bill / 2

    # b is the bill charged and difference is what Brian owes Anna
    difference = b - actual_bill_per_person
    if difference == 0:
        print("Bon Appetit")
    else:
        print(int(difference))
    


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit([bill], k, b)
