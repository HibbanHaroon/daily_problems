# data = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 
#         "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 
#         "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#         "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#         "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#         "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day4-PartOne/input.txt', 'r')
data = f.readlines()
arr = []

for i, line in enumerate(data):
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

    count_matching = 0
    for num in my_numbers:
        if num in winning_numbers:
            count_matching += 1

    # For Original
    index = i + 1
    arr.append(index)
    for j in range(0, count_matching):
        index += 1
        arr.append(index)

    # For copies
    index = i + 1
    for j in range(arr.count(index) - 1):
        index = i + 1
        for k in range(0, count_matching):
            index += 1
            arr.append(index)
count = 0
for i in range(len(data)):
    count = count + arr.count(i + 1)

print(count)
