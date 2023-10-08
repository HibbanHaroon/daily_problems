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
    temp_ranked = ranked
    player_rankings = []
    for player_score in player:
        temp_ranked.append(player_score)
        temp_ranked = set(temp_ranked)
        temp_ranked = list(sorted(temp_ranked, reverse=True))
        player_ranking = temp_ranked.index(player_score) + 1
        player_rankings.append(player_ranking)

    return player_rankings

if __name__ == '__main__':

    # ranked_count = int(input().strip())

    # ranked = list(map(int, input().rstrip().split()))

    # player_count = int(input().strip())

    # player = list(map(int, input().rstrip().split()))

    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]

    result = climbingLeaderboard(ranked, player)
    print(result)

    # print('\n'.join(map(str, result)))
    # print('\n')


""" 
The code for now is returning the final ranked list. But, I haven't added the logic of finding the rankings from this list.
"""