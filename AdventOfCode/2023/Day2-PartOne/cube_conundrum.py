# data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

possible_games = []
rule = {'red': 12, 'green': 13, 'blue': 14}

f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day2-PartOne/input.txt', 'r')

for line in f.readlines():
    game_str, *rest = line.split(": ")
    game_no_list = []
    for char in game_str:
        if char.isnumeric():
            game_no_list.append(char)
    
    game_no_str = "".join(game_no_list)
    game_no = int(game_no_str)

    cubes = rest[0].split("; ")

    is_game_possible = True
    for cube_no, cube in enumerate(cubes):
        ball_str = cube.split(", ")
        for balls in ball_str:
            ball_no, ball_colour = balls.split(" ")
            ball_colour = ball_colour.strip()
            ball_no = int(ball_no)

            if ball_no > rule[ball_colour]:
                is_game_possible = False
                break
    
    if is_game_possible == True:
        possible_games.append(game_no)

print(sum(possible_games))