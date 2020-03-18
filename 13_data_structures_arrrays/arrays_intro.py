# Creating a Dynamic Array: 
import time
class DynamicArray:
    def __init__(self,capacity = 0):
        self.capacity = capacity 
        self.count = 0
        self.storage = [None] * capacity 
    
    def insert(self, index, value):
        # First pass solution
        # self.storage[index] = value
        # NB: range() can go in reverse range (4,0,-1)
        if self.count == self.capacity:
            self.double_size()
            return "Array is full but we made it bigger"
        
        for idx in range(self.count, index, -1):
            self.storage[idx] = self.storage[idx - 1]
        
        self.storage[index] = value 
        self.count += 1
    
    def append(self, value):

        if self.count == self.capacity:
            self.double_size()
            return "Array is full but we made it bigger"
        
        self.storage[self.count] = value
        self.count += 1

    def double_size(self):
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity

        # copy everything over 
        for i in range(self.count):
            new_arr[i] = self.storage[i]
        
        self.storage = new_arr

# O(n^2)
def add_to_front(n):
    x = []
    for i in range(n):
        x.insert(i, n-1)
    return x

# O(n), python will handle resizing; every once in a while, we will have to resize
def add_to_back(n):
    x = []
    for i in range(n):
        x.append(n) #This is O(1)
    return x


def preallocate(n):
    x = [None] * n
    for i in range(n):
         x[i] = i
    return x

# Quick test:
n = 5000
start_time = time.time()
add_to_front(n)
end_time = time.time()
print("Time to add to front", end_time-start_time)




    