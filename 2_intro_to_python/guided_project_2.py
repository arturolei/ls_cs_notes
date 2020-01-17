# Problem Solving Framework, 
""" Intro to Python II - Guided Project
    This document contains examples for CS Intro to Python, module 2. Examples
    will highlight unique syntax rules in Python. Students will continue to
    practice creating elements such as lists, dictionaries, and functions. 
    Additionally, we will look at the CS problem-solving framework and practice
    using it to break down more complex problems.
"""
# RECAP: How do we...

# create a list of floating point temperatures?
# TODO

# in a single line, create a new list containing all of the temperatures from
# the above list that are greater than 90.0?
# TODO

# create a dictionary students in which their `id` is the key and their name
# is the `value`?
students = {}
students.update({22:"tom"})
students[3343434]="George"

print(students)

# add a new student to our dictionary? modify an existing student entry?
# Add a new student 
students.update({23:'Steven'})
print('after student added via "update"', students)

# Update/modify student entry
students[22] = "Irene"
print(students)

# When we write functions in different languages, it is important to know if
# arguments are passed by REFERENCE or VALUE; python is passing by value?

n = 5
nums = [1,2,3]

def mult2(x): # x is a single integer value to be doubled
    return x * 2

print(mult2(n))


def mult2_list(x): # x is a list of integer values to be doubled
    for i in range(len(x)):
        x[i] *= 2
    #return x #this actually isn't necessary; lists and dictionary are passed as reference
mult2_list(nums)
print('mult2_list result',nums)

# UPER - Given a number of people, number of pizzas, and number of slices per
# pizza, write a function to evenly divide the slices between each person.
# 1. Understand
# - How do we know #'s? We get functions passed in args?
# - Is everyone eating? (yes)
# - Per discussion, you can only eat whole slices (so maybe we need to "floor things")
# - Cost per slice? I don't think this is necessary 
# - What is our output format going to be like? 
# - Return slices per person? What do we do with the extras? (Sacrifice to the Gods?)
# - Return slices per person plus number left over that no gets

# 2. Plan
# Need a function that takes three arguments in a particular order, num_people, num_pizzas, num_slices
# Need a way to handle edge cases 

# 3. Execute
def divide_pizza(number_people, number_pizzas, number_slices):
    # Find total number of slices then divide and find reminder
    total_slices_count = number_pizzas * number_slices 
    slice_per_person = total_slices_count//number_people
    leftovers = total_slices_count % number_people
    return f'Each person gets {slice_per_person} slices, and there are {leftovers}'

print(divide_pizza(4,2,8)) # four slices per person, 0 leftovers
print(divide_pizza(5,3,8)) # four slices per person, 4 leftovers

# 4. Reflect
# - Error handling 
# - Validating input


# UPER - Prompt a user to enter three, unique numbers as input, print out 
# which number is the largest of the three. 

# 1. Understand
# We are going to get three numbers (in some form, list or just straight three parameters)
# Numbers are all going to be unique 
# I'm assuming that they are all "real"/rational numbers (no "imaginary" numbers, e.g. i)
# Careful input originally given as string if we use input()
# What are the possible the ranges? What kinds of numbers (float() vs int())

# 2. Plan
# I'm tempted use in-built method (list, sort()), how 
# Massaging inputs/getting the inputs into a form that we can use 
# max (built-in)

# 3. Execute
def calc_largest(num_list):
    return f"This is the max: {max(num_list)}"

print('Start')
my_num_list = []
num1 = input('Give me number 1: ')
my_num_list.append(float(num1))

num2 = input('Give me number 2: ')
my_num_list.append(float(num2))

num3 = input('Give me number 3: ')
my_num_list.append(float(num3))

print(my_num_list)
print(calc_largest(my_num_list))

# 4. Reflect
# No error handling
# No validation of inputs
# Using built-in max might not be best

# UPER - Write a function that returns the "centered" average of an array of 
# ints, which we'll say is the mean average of the values, except ignoring the 
# largest and smallest values in the array. 
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3
# 1. Understand
# 2. Plan
# 3. Execute
#def centered_average(nums):
    # TODO
 #   pass
# 4. Reflect