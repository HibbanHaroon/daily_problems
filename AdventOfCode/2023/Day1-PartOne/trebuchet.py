calibrated_document = []

f = open('D:/Coding/Daily Problems/AdventOfCode/2023/Day1-PartOne/file.txt', 'r')
for text in f.readlines():
    calibration_value = None
    temp = None

    for char in text:
        if calibration_value == None and char.isnumeric() == True:
            calibration_value = int(char)
        elif char.isnumeric() == True:
            temp = int(char)

    if temp != None:
        calibration_value = (10 * calibration_value) + temp
    else:
        calibration_value = (10 * calibration_value) + calibration_value

    calibrated_document.append(calibration_value)

print(sum(calibrated_document))
