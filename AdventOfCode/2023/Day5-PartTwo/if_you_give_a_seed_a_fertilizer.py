# I have no idea why am I getting a wrong solution here where my logic is correct. 
# My approach is bruteforce yes, but I can't think of any other solution
# I will try to debug it some other day.

data = []

# Read input from file
with open('D:/Coding/Daily Problems/AdventOfCode/2023/Day5-PartOne/input1.txt', 'r') as file:
    lines = file.readlines()
    data.append(lines)

data = data[0]
seeds_str = data[0]
_, seeds_arr = seeds_str.split(': ')
seeds_arr = [int(string) for string in seeds_arr.split()]

seeds = []
temp_seeds = []
count = 0
for seed in seeds_arr:
    if count == 0:
        temp_seeds.append(seed)
        count += 1
    elif count == 1:
        temp_seeds.append(seed)
        s1 = temp_seeds[0]
        s2 = temp_seeds[1]
        seeds.append((s1, s2))

        temp_seeds.clear()
        count = 0

data.pop(0)
data.remove('\n')

arr = []
dictionary = {}
for line in data:
    line = line.strip()

    if line != '':
        arr.append(line)
    else:
        name_arr = arr[0].split()[0]
        num_arr = arr[1:]
        new_num_arr = []
        for string in num_arr:
            new_num_arr.append([int(st) for st in string.split()])

        dictionary[name_arr] = new_num_arr
        arr = []

# For the last thing in arr
name_arr = arr[0].split()[0]
num_arr = arr[1:]
new_num_arr = []
for string in num_arr:
    new_num_arr.append([int(st) for st in string.split()])

dictionary[name_arr] = new_num_arr

seed_to_soil_map = dictionary['seed-to-soil']
soil_to_fertilizer_map = dictionary['soil-to-fertilizer']
fertilizer_to_water_map = dictionary['fertilizer-to-water']
water_to_light_map = dictionary['water-to-light']
light_to_temperature_map = dictionary['light-to-temperature']
temperature_to_humidity_map = dictionary['temperature-to-humidity']
humidity_to_location_map = dictionary['humidity-to-location']

# Print or use the extracted information as needed
# print("Seeds:", seeds)
# print("Seed-to-soil map:", seed_to_soil_map)
# print("Soil-to-fertilizer map:", soil_to_fertilizer_map)
# print("Fertilizer-to-water map:", fertilizer_to_water_map)
# print("Water-to-light map:", water_to_light_map)
# print("Light-to-temperature map:", light_to_temperature_map)
# print("Temperature-to-humidity map:", temperature_to_humidity_map)
# print("Humidity-to-location map:", humidity_to_location_map)

def get_item(item, item_mapping):

    range_found = False
    for destination, source, range_length in item_mapping:
        if item >= source and item < (source + range_length):
            range_found = True
            return destination + abs(item - source)

    if range_found == False:
        return item

minimum_location = float('inf')

for seed_pair in seeds:
    for seed in range(seed_pair[0], seed_pair[0] + seed_pair[1]):
        soil = get_item(seed, seed_to_soil_map)
        fertilizer = get_item(soil, soil_to_fertilizer_map)
        water = get_item(fertilizer, fertilizer_to_water_map)
        light = get_item(water, water_to_light_map)
        temperature = get_item(light, light_to_temperature_map)
        humidity = get_item(temperature, temperature_to_humidity_map)
        location = get_item(humidity, humidity_to_location_map)
        
        if minimum_location > location:
            minimum_location = location

print("Minimum : ", minimum_location)


# Old Logic

# def get_item(item, item_mapping):
#     item_dict = {}
    
#     for mapping in item_mapping:

#         source = mapping[1]
#         destination = mapping[0]
#         range_length = mapping[2]

#         for i in range(range_length):
#             item_dict[source] = destination
#             source += 1
#             destination += 1

#     if item not in item_dict.keys():
#         return item
#     else:
#         return item_dict[item]
