"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number 1 on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number. 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    player_rankings = []
    ranked = list(set(ranked))
    ranked = sorted(ranked, reverse=True)

    # Since the player array is in ascending order, we'll check if the player score can be placed at the end of the ranked array
    # If not then pop the last element in the ranked array. 
    # If you have found that the player score can be inserted at the end of the ranked array, 
    # then the length of the array + 1 will be the rank of the player score (plus one because the score will go after the current array)
    for player_score in player:
        while ranked and player_score >= ranked[-1]:
            ranked.pop()
        player_rankings.append(len(ranked) + 1)

    return player_rankings

if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    # ranked = [100, 100, 50, 40, 40, 20, 10]
    # player = [5, 25, 50, 120]

    result = climbingLeaderboard(ranked, player)
    print(result)

    # print('\n'.join(map(str, result)))
    # print('\n')


""" 
Since my code wasn't passing some test cases due to time complexity, I took inspiration from a solution I found on Hackerrank forum.
"""