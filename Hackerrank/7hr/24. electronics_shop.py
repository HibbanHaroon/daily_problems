"""
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. 
Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible 
to buy both items, return -1. 
"""

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    maximum = 0
    if len(keyboards) > 0 and len(drives) > 0:
        for keyboard in keyboards:
            for drive in drives:
                if keyboard + drive <= b:
                    if maximum < keyboard + drive:
                        maximum = keyboard + drive
    
    if maximum == 0:
        return -1
    else:
        return maximum

if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent) + '\n')
