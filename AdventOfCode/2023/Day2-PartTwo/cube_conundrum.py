# Find Max of each cube for each game
# Multiply the max of cubes for each game
# Then for each game, simply sum the multiplied thing.

products = []

f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day2-PartOne/input.txt', 'r')

for line in f.readlines():
    game_str, *rest = line.split(": ")

    cubes = rest[0].split("; ")

    maximum_ball_nos = {}

    for cube_no, cube in enumerate(cubes):
        ball_str = cube.split(", ")
        for balls in ball_str:
            ball_no, ball_colour = balls.split(" ")
            ball_colour = ball_colour.strip()
            ball_no = int(ball_no)

            if ball_colour not in maximum_ball_nos:
                maximum_ball_nos[ball_colour] = ball_no
            else:
                if ball_no > maximum_ball_nos.get(ball_colour):
                    maximum_ball_nos[ball_colour] = ball_no

    product = 1
    for ball_nos in maximum_ball_nos.values():
        product *= ball_nos

    products.append(product)

# print(products)
print(sum(products))

# Takeaways from this problem:
"""
game_str, *rest = line.split(": "). This is amazing, if I had just written this line without the *, 
I would have gotten an unpacking error. However, I used *, it allowed me to actually unpack the list in a way that
the first element goes to game_str and the rest of the elements goes in rest. 

strip was another useful function I used, it helped me remove \n at the end of the color such as 'red\n'
"""