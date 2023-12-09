f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day9-PartOne/input1.txt', 'r')

data = f.readlines()

sum_extrapolated = 0
for line in data:
    line = line.strip()
    numbers = line.split()
    numbers = [int(string) for string in numbers]

    first_numbers = []
    first_numbers.append(numbers[0])

    while all(element == 0 for element in numbers) == False:
        temp = []
        for i in range(len(numbers) - 1):
            temp.append(numbers[i + 1] - numbers[i])
        
        numbers = temp
        first_numbers.append(numbers[0])                                                                            
    
    first_numbers.reverse()

    difference = 0
    for num in first_numbers:
        difference = num - difference

    sum_extrapolated += difference

print(sum_extrapolated)

# Takeaways:
# while all(element == 0 for element in numbers) == False: 
# Using this function was very informative, this function basically returns True
# If all the elements in a list is a certain element which I am checking by element == certain_number
