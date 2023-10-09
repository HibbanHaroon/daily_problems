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
    player_ranking = []
    for player_score in player:
        new_ranked = []
        n = len(ranked)
        player_score_added = False
        i = 0
        while i < n:
            if ranked[i] <= player_score and player_score_added == False:
                new_ranked.append(player_score)
                player_score_added = True
                i -= 1
            else:
                new_ranked.append(ranked[i])

            i += 1

        # The player score is the smallest and will be appended at the end
        if player_score_added == False:
            new_ranked.append(player_score)

        ranked = new_ranked

    return ranked


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    # ranked = [100, 100, 50, 40, 40, 20, 10]
    # player = [5, 25, 50, 120]

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
    print('\n')


""" 
The code for now is returning the final ranked list. But, I haven't added the logic of finding the rankings from this list.
"""