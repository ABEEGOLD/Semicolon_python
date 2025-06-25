import random

numbers = []

def number_within(number):
    for index in range(1,11):
        number  = random.randint(1, 51)
        numbers.append(number)


def length_list(numbers):
    total = 0
    for index in numbers:
        length = 0
        length = length + 1
        total += length
    return total


def sum_elements_at_even_position(numbers):
    sum_even = 0
    for index in numbers:
        if index % 2 == 0:
            sum_even += index
    return sum_even


def sum_elements_at_odd_position(numbers):
    sum_odd = 0
    for index in numbers:
        if index % 2 != 0:
            sum_odd += index
    return sum_odd

def multiply_elements_at_third_position(numbers):
    multiply = 1
    counter = 0
    for index in numbers:
        if index % 3 == 0:
            multiply *= index
    return multiply

def calculate_the_average_of_all_elements_list(numbers):
    total = 0
    for index in numbers:
        total += index
    average = total / length_list(numbers)
    return average




