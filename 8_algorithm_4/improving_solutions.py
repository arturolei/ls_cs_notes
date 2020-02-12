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

# Run time, 