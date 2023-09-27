"""
HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

# Logic/Explanation
# Has to be between 0 and 100 inclusive
# less than 38 (or 40 as 38 - 40 is less than 3, so it will round off)
# (43 - 45) < 3 then make 43 -> 45
# (42 - 45) < 3 then it stays 42
# Remove the array by removing the grade which is failed


def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        if not (grade < 0 or grade > 100):
            if not grade < 38:
                next_multiple = ((grade//5) + 1) * 5
                difference = next_multiple - grade
                if difference < 3:
                    final_grades.append(next_multiple)
                else:
                    final_grades.append(grade)
            else:
                final_grades.append(grade)
        else:
            final_grades.append(grade)

    return final_grades
            



if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
    print('\n')
