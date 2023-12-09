from itertools import product
import math

def check_in_bounds(row, col, row_n, col_n):
    return 0 <= row <= row_n and 0 <= col <= col_n

def is_symbol(char):
    return True if char.isalnum() == False and char != '.' else False
    
def find_number_and_mid_index(row, col):
    start_index = col
    end_index = col

    num_list = []
    line = data[row]
    num_list.append(line[col])

    index = col - 1
    while(line[index].isdigit()):
        num_list.insert(0, line[index])
        start_index = index
        index -= 1
    
    index = col + 1
    while(line[index].isdigit()):
        num_list.append(line[index])
        end_index = index
        index += 1
    
    num = int("".join(num_list))
    mid_index = math.floor((start_index + end_index) / 2)
    return (num, (row, mid_index))

# data = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", ".....+.58.", "..592.....", "......755.", "...$.*....", ".664.598.."]
f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day3-PartOne/input.txt', 'r')

directions = set(product([-1, 0, 1], repeat=2)) - {(0, 0)}

part_numbers = {}

data = f.readlines()

for line_no, line in enumerate(data):
    line = line.strip()
    for char_no, char in enumerate(line):
        length = len(line)
        if is_symbol(char):
            for row, col in directions:
                new_row = row + line_no
                new_col = col + char_no
                if check_in_bounds(new_row, new_col, len(data), len(line)) and data[new_row][new_col].isdigit():
                    num, mid_index = find_number_and_mid_index(new_row, new_col)
                    part_numbers[mid_index] = num
            
print(sum(part_numbers.values()))

# Problem:
# 1. I have to get the whole number which the digit is from - Resolved
# 2. I have to remove any duplicates that I may add - Resolved
# 3. If two symbols point to one number. Not done.

# New Approach:
# I have a new approach in mind where each number will have a unique indentifier which will be the 
# middle point index i.e., using the starting and the ending index of that number to get the middle index.
# This will solve my problem if any two symbols are pointing to one number or any other problem. 

# The new approach worked. Shoutout to my pookie bear for giving this idea of creating a dictionary with 
# every number having a unique identifier.