''' Intro to Python I - Guided Project
    This document contains examples for CS Intro to Python, module 1. Examples
    focus on Python syntax & semantics plus the usage of lists, dicts, sets,
    and tuples.
'''
# How do we print something to the console?
print("Hello, world!")

# NB: Single quotes are okay 
print("'Hello, Watson!' said Sherlock Holmes")

# With f-strings?
world = "world/mondo"
print(f"Hello, {world}!!!")

# Given an "out" string length 4, such as "<<>>", and a word, return a new 
# string where the word is in the middle of the out string, e.g. "<<word>>".
# (from CodingBat)
def make_out_word(out, word):
    return f"{out[0:2]}{word}{out[2:]}"

print(make_out_word('<<>>', 'Yay')) # → '<<Yay>>'
print(make_out_word('<<>>', 'WooHoo')) # → '<<WooHoo>>'
print(make_out_word('[[]]', 'word')) # → '[[word]]'


# Given an array of ints length 3, return the sum of all the elements.
# (from CodingBat)
def sum3(nums):
    if len(nums) == 3:
        return sum(nums) #alt solution nums[0]+nums[1]+nums[2]
    else:
        return "error" #input array is too big or wrong size

print(sum3([1, 2, 3])) # → 6
print(sum3([5, 11, 2])) # → 18
print(sum3([7, 0, 0])) # → 7
print (sum3([1,2,3,5])) # -> error

# Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 7 (every 6 will be followed by at 
# least one 7). Return 0 for no numbers.
# (from CodingBat)

def sum67(nums):
    summed_numbers = 0
    seven_found= False
    six_found = False
    for number in nums:
      
        if number == 6:
            summed_numbers+=0
            six_found = True
        elif number == 7:
            summed_numbers+=0
            seven_found = True 
        else:
            if seven_found == True and six_found == True or seven_found == False and six_found == False:
                summed_numbers+=number
            else:
                summed_numbers+=0   
    return summed_numbers

print(sum67([1, 2, 2])) # → 5
print(sum67([1, 2, 2, 6, 99, 99, 7])) # → 5
print(sum67([1, 1, 6, 7, 2])) # → 4


# Create a new list containing the squares of all values in `numbers`with a 
# list comprehension
numbers = [1, 2, 3, 4, 5]
print(numbers)
print('Numbers squared', [x**2 for x in numbers])

# the equivalent of...
numbers_squared = []
for num in numbers:
    numbers_squared.append(num**2)

print('Numbers squared the long way',numbers_squared)



# We can also use list comprehensions to filter!
# Create a new list containing only the even values of `numbers`

print('filtered numbers, list comprehension', [x for x in numbers if x % 2 == 0])

# the equivalent of...
numbers_filtered = []

for num in numbers:
    if num % 2 == 0:
        numbers_filtered.append(num)

print('Loop with for loop', numbers_filtered)

# Can you use pieces of both of the above examples to...
# Create a new list containing only the names that start with `s` so that they 
# are properly capitalized (regardless of how the name originally appears) 
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

print(names)
print([name[0].upper()+name[1:] for name in names if name[0].lower() == 's'])

# Misc Notes:
# Strings are immutable 

## Dictionaries 
my_dict = {'name':'Sherlock', 'job':'Consulting Detective'}
## Dictionaries are not ordered? 

# Set, unordered, no dup allowed

# Tuples, immutable list, ordered
students = ('student1', 'student2')
