f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day6-PartOne/input1.txt', 'r')

data = f.readlines()
arr = []
for line in data:
    line = line.strip()
    _, rest = line.split(':')
    arr.append(rest.split())
    
times = arr[0]
distances = arr[1]

times = [int(string) for string in times]
distances = [int(string) for string in distances]

product = 1

for total_time, total_distance in zip(times, distances):
    no_of_wins = 0
    for speed in range(total_time + 2):
        time = abs(speed - total_time)
        distance = speed * time
        if distance > total_distance:
            no_of_wins += 1
            
    product *= no_of_wins

print(product)
        