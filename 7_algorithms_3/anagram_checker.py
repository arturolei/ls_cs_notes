
# Check lecture recording 

def anagram_checker(str1, str2):
    # constraints: strings only, single words, len < 50 chars for input 
    # return: True, False 
    # ex. tone, note 
    # Is this a sorting problem? How so? ---> Sort inputs so they are both in order
    # Things to consider: same letters--> same length 
    if str1.split().sort() == str2.split().sort():
        return True
    else:
        return False 


# a celebrity is a person 1) who knows no one but ii) knows every one knows
# quick solution 

def find_celebrity(people):
    for i in range(len(people)):
        if len(people[i].known) == 0:
            return i

def recursive_find_celebrity(people): #This is big O(n) like other
    if len(people[0].known) == 0:
        return people[0]
    else:
        return recursive_find_celebrity(people[1:])


# Fibonnaci, Fibonnacci, is O(2^n)
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Things to consider:
# IS this a sorting issue?
# Can I eliminate or reduce the input?