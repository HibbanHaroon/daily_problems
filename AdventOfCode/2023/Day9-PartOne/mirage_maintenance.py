f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day9-PartOne/input.txt', 'r')

data = f.readlines()

sum_extrapolated = 0
for line in data:
    line = line.strip()
    numbers = line.split()
    numbers = [int(string) for string in numbers]

    last_numbers = []
    last_numbers.append(numbers[len(numbers) - 1])

    while all(element == 0 for element in numbers) == False:
        temp = []
        for i in range(len(numbers) - 1):
            temp.append(numbers[i + 1] - numbers[i])
        
        numbers = temp
        last_numbers.append(numbers[len(numbers) - 1])
    
    sum_extrapolated += sum(last_numbers)

print(sum_extrapolated)