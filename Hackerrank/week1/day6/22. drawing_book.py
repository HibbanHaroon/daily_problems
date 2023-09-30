"""
A teacher asks the class to open their books to a page number. A student can either start turning pages from the 
front of the book or from the back of the book. They always turn pages one at a time. When they open the book, 
page  is always on the right side:
When they flip page , they see pages  and . Each page except the last page will always be printed on both sides. 
The last page may only be printed on the front, given the length of the book. If the book is  pages long, 
and a student wants to turn to page , what is the minimum number of pages to turn? They can start at the 
beginning or the end of the book. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    front_steps = p // 2

    steps_to_last_page = n // 2
    back_steps = steps_to_last_page - front_steps 

    if front_steps < back_steps:
        return front_steps
    else:
        return back_steps

if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(str(result) + '\n')
