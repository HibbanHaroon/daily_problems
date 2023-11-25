""" 
You will be given a square chess board with one queen and a number of obstacles placed on it. 
Determine how many squares the queen can attack.
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

# This function will help us in checking whether a row and a column lies inside the board.
# It will return true if the row, col lies inside the board.
def inBoard(row, col, n):
    return 1 <= row <= n and 1 <= col <= n


def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0

    # This will make tuples of obstacles and remove any duplicates.
    obstacles_set = set([(row, col) for row, col in obstacles])

    # This will make a set of all the possible directions a queen can go such as up(1, 0), down(-1, 0), up-left diagonal (1, -1), ...
    # Removing (0,0) from the set as the queen is not gonna stay one position, we are looking for directions to go here.
    directions = set(product([-1, 0, 1], repeat=2)) - {(0, 0)}

    # Now we will iterate for each direction and check all the cells that we visit and then count them.
    for row, col in directions:
        # Visitable cells is a list of all cells inside the board we can go from the queen's position.
        # For example, if the queen is at (3,3) and the direction is up (1,0). We will iterate from 1 to n + 1(cause n is inclusive)
        # and check if the cell is inside the board if it, and then tuple is placed in this vistableCells list.
        # r_q + row * index means that if queen is at row 3, and row of direction is 1, tuples from index 1 to n would be
        # (3 + 1 * 1, 3 + 0 * 1) = (4, 3), (3 + 1 * 2, 3 + 0 * 2) = (5, 3), the next tuple won't be inside the board.
        visitableCells = [(r_q + row * index, c_q + col * index) for index in range(1, n + 1) if inBoard(r_q + row * index, c_q + col * index, n)]
        
        # We are basically placing a False if a tuple in the visitableCells is also an obstacle
        # So the bool_list can look something like this [True, False, True]
        bool_list = [(row, col) not in obstacles_set for row, col in visitableCells]
        
        # If there is a false in a list, then we get the index and simply add that index to the count.
        # This means that [True, False, True] -> False is at index 1, only 1 cell can be attacked i.e., the first True cell
        # Any True cell after False cannot be attacked.
        # If there are no False in a list, then [True, True] then the length would be 2, implying both 2 cells can be attacked.
        if False in bool_list:
            num = bool_list.index(False)
            count += num
        else:
            count += len(bool_list)

    return count


if __name__ == '__main__':

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # second_multiple_input = input().rstrip().split()

    # r_q = int(second_multiple_input[0])

    # c_q = int(second_multiple_input[1])

    # obstacles = []

    # for _ in range(k):
    #     obstacles.append(list(map(int, input().rstrip().split())))

    n = 5
    k = 3

    r_q = 4 
    c_q = 3

    obstacles = [[5, 5], [4, 2], [2, 3]]

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + '\n')
