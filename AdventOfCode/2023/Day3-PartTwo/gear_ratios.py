from itertools import product

def check_in_bounds(row, col, row_n, col_n):
    return 0 <= row <= row_n and 0 <= col <= col_n
    
def find_number(row, col):
    num_list = []
    line = data[row]
    num_list.append(line[col])

    index = col - 1
    while(line[index].isdigit()):
        num_list.insert(0, line[index])
        index -= 1
    
    index = col + 1
    while(line[index].isdigit()):
        num_list.append(line[index])
        index += 1
    
    num = int("".join(num_list))
    return num

# data = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", ".....+.58.", "..592.....", "......755.", "...$.*....", ".664.598.."]
f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day3-PartOne/input.txt', 'r')

directions = set(product([-1, 0, 1], repeat=2)) - {(0, 0)}

gear_ratios = []

data = f.readlines()

for line_no, line in enumerate(data):
    line = line.strip()
    for char_no, char in enumerate(line):
        length = len(line)
        if char == '*':
            gear_arr = []
            for row, col in directions:
                new_row = row + line_no
                new_col = col + char_no
                if check_in_bounds(new_row, new_col, len(data), len(line)) and data[new_row][new_col].isdigit():
                    num = find_number(new_row, new_col)
                    if num not in gear_arr:
                        gear_arr.append(num)

            if len(gear_arr) == 2:
                gear_ratio = gear_arr[0] * gear_arr[1]
                gear_ratios.append(gear_ratio)
            
print(sum(gear_ratios))

