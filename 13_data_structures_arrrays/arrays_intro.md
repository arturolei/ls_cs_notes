# Intro to Hashtables, Blockchain, and Arrays, 10 March 2020 

## Hashtables or a Hash Map
- Hash tables are like dictionaries, a collectiono of mappings of keys to values
- Constant time (O(n)) to add or to remove from a hash table 
- You can think of a Hash table as made up of:
  - an array, [] 
  - A hash function, f()

## Some Things to Know About Arrays: 
- Everything you need to know about arrays is that live/occupy space in memory; "they live somewhere on your computer hard drive"
- When you make a new array, you get a pointer to a slot in computer memory. 
- Adding to end of array is O(1)
- Adding to start of an array is O(n)
- Note in some languages (e.g. Python, JS), you can add easily to the end of the array because the language by default allocates extra memory space to you when you build an array
  - A dynamic array will handle for you, getting more space for when it is filled up. 

## Pre-Allocation: 


## Hash Functions:
- Take in a string and turn it into an index we can use. 
- Hash function takes in a key and spits out a value?; we can then use to create something that we put into an array 
- Storing strings in constant time --> This is a big advantage


## Hash Tables: 
- USe of linked lists if we have a "collision"