# Linked Lists 

#HackerRank, https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    return a[::-1] # Simple solution 
    """
    Approach 3: Manipulate original array
    1. Start outside 
    2. Move to middle, swap left and right
    3. Continue until there is nothing left

    Approach 2: Build new array
    Loop through backwards and create new loop
    new_a = []

    for i in range(len(a)-1, -1, -1):
        new_a.append(a[i])

    Approach 3:
    for i in range (0, len(a)//2):
        a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]
    return a


    """
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
"""

# Singly Linked List 
# - Singly Linked Lists are made of Nodes that have a value and a pointer
# - If next = None, we have end of linked list

## Doubly Linked List (DLL)
# - Value
# - Pointer to next 
# - Pointer to previous