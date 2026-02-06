def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area, perimeter = calc_rectangle(length, width)
print(f"Area: {area}, Perimeter: {perimeter}")

def power(base, exp):
    """Return base raised to the power of exp."""
    return base ** exp

def average(numbers_list):
    """Return the average of a list of numbers."""
    return sum(numbers_list) / len(numbers_list)

import math_operationsD5T2
result_power = math_operationsD5T2.power(28, 67)
result_avg = math_operationsD5T2.average([12, 320, 5530, 40])
print(f"2^10 = {result_power}")
print(f"Average = {result_avg}")