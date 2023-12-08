f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day4-PartOne/input.txt', 'r')
data = f.readlines()

points = []

for line in data:
    _, rest = line.split(": ")
    winning_numbers_str, my_numbers_str = rest.split(" | ")
    
    winning_numbers = []
    number_str = ""
    for char in winning_numbers_str:
        if char.isnumeric():
            number_str = number_str + char
        elif char == ' ':
            if number_str != "":
                winning_numbers.append(int(number_str))
                number_str = ""
    
    # Appending the last number
    winning_numbers.append(int(number_str))
    # print(winning_numbers)
    
    my_numbers = []
    number_str = ""
    for char in my_numbers_str:
        if char.isnumeric():
            number_str = number_str + char
        elif char == ' ':
            if number_str != "":
                my_numbers.append(int(number_str))
                number_str = ""
    
    # Appending the last number
    my_numbers.append(int(number_str))
    # print(my_numbers)

    point = 0
    for num in my_numbers:
        if num in winning_numbers:
            if point == 0:
                point = 1
            else:
                point = point * 2
    
    points.append(point)

print(sum(points))