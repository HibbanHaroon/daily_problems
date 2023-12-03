digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

calibrated_document = []

f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day1-PartOne/file.txt', 'r')

for text in f.readlines():
    indexes_dict = {}
    for digit in digits:
        first_index = text.find(digit)
        last_index = text.rfind(digit)
        
        temp_list2= []
        if first_index >= 0:
            if first_index != last_index:
                temp_list2.append(first_index)
                temp_list2.append(last_index)
            else:
                temp_list2.append(first_index)

        if digits[digit] not in indexes_dict:
            if len(temp_list2) > 0:
                indexes_dict[digits[digit]] = temp_list2
        else:
            temp_list = indexes_dict[digits[digit]]
            temp_list.append(temp_list2)
            indexes_dict[digits[digit]] = temp_list

    for index, char in enumerate(text):
        if char.isnumeric() == True:
            if int(char) not in indexes_dict:
                temp_list = []
                temp_list.append(index)
                indexes_dict[int(char)] = temp_list
            else:
                temp_list = indexes_dict[int(char)]
                temp_list.append(index)
                indexes_dict[int(char)] = temp_list

    indexes_list = []

    for lists in indexes_dict.values():
        for value in lists:
            indexes_list.append(value)

    minimum_index = min(indexes_list)
    maximum_index = max(indexes_list)
    minimum = None
    maxmimum = None

    for key, value in indexes_dict.items():
        if minimum_index in value:
            minimum = key
        elif maximum_index in value:
            maxmimum = key

    calibration_value = minimum
    if maxmimum != None:
        calibration_value = (10 * calibration_value) + maxmimum
    else:
        calibration_value = (10 * calibration_value) + calibration_value

    calibrated_document.append(calibration_value)

print(sum(calibrated_document))
