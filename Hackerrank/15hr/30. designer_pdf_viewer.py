"""
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. 
In this PDF viewer, each word is highlighted independently. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    maximum = 0
    for letter in word:
        ascii_value = ord(letter)
        index = ascii_value - 97
        if maximum < h[index]:
            maximum = h[index]
        
    return maximum * len(word)

if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')
