# HashFunction 
# Determinatistic: for given input, output will always be the same 
# Defined output range:m for a hash table of size 16, all keys must hash to value of 0 to 15
# Predicatable Speed: Hash functions for hash tables should be lighting fast; constant time?
# non-invertible: you should not be able to reconstruct the input value from the output

def myFakeHash(word):
    hash = len(word)
    return hash % 7 #or an array

#myFakeHash('Timothy') #--> 7 
#myFakeHash('sevenns') #--> 7

# scramble the key and come up with very different values (avoid having same values)
def djb2(key):
    # start from large prime number
    # We want to avoid collisions
    hash_value = 5381
    for char in key:
        # randomly scrambling the value
        hash_value = hash_value + (hash_value << 5) + char 
    return hash_value


# You can think of a Hash Table as really being a hash table and a hash function
# Hash functions in essense turn a string into a number