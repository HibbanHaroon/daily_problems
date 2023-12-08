from itertools import product

def check_in_bounds(row, col, row_n, col_n):
    return 0 <= row <= row_n and 0 <= col <= col_n

def is_special_character(char):
    if char.isalnum() == False and char != '.':
        return True
    else: 
        return False
    
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

part_numbers = []

data = f.readlines()

for line_no, line in enumerate(data):
    line = line.strip()
    for char_no, char in enumerate(line):
        length = len(line)
        if char.isalnum() == False and char != '.':
            line_up = {}
            line_down = {}
            for row, col in directions:
                new_row = row + line_no
                new_col = col + char_no
                if check_in_bounds(new_row, new_col, len(data), len(line)) and data[new_row][new_col].isdigit():
                    if row == -1:
                        line_up[(new_row, new_col)] = find_number(new_row, new_col)
                    elif row == 1:
                        line_down[(new_row, new_col)] = find_number(new_row, new_col)
                    else:
                        part_numbers.append(find_number(new_row, new_col))
            
            if len(line_up) == 1:
                part_numbers.extend(line_up.values())
            elif len(line_up) == 2:
                keys = list(line_up.keys())
                for i in range(len(line_up) - 1):
                    key1 = keys[i]
                    key2 = keys[i + 1]
                    row1, col1 = key1
                    row2, col2 = key2

                    if abs(col1 - col2) == 1:
                        part_numbers.append(line_up[key1])
                        
                    elif abs(col1 - col2) == 2 and line[max(col1, col2) - 1] == '.':
                        part_numbers.append(line_up[key1])
                        part_numbers.append(line_up[key2])
            elif len(line_up) == 3:
                part_numbers.extend(set(line_up.values()))
                

            if len(line_down) == 1:
                part_numbers.extend(line_down.values())
            elif len(line_down) == 2:
                keys = list(line_down.keys())
                for i in range(len(line_down) - 1):
                    key1 = keys[i]
                    key2 = keys[i + 1]
                    row1, col1 = key1
                    row2, col2 = key2
                    
                    if abs(col1 - col2) == 1:
                        part_numbers.append(line_down[key1])
                    elif abs(col1 - col2) == 2 and line[max(col1, col2) - 1] == '.':
                        part_numbers.append(line_down[key1])
                        part_numbers.append(line_down[key2])
            elif len(line_down) == 3:
                part_numbers.extend(set(line_down.values()))
                

print(sum(part_numbers))

# Problem:
# 1. I have to get the whole number which the digit is from - Resolved
# 2. I have to remove any duplicates that I may add - Resolved
# 3. If two symbols point to one number. Not done.

# New Approach:
# I have a new approach in mind where each number will have a unique indentifier which will be the 
# middle point index i.e., using the starting and the ending index of that number to get the middle index.
# This will solve my problem if any two symbols are pointing to one number or any other problem. 
