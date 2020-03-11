import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #if the new value is smaller than the existing node
        if value < self.value:
            #if not left  means "if left is null"
            if not self.left:
                #create a new node
                self.left = BinarySearchTree(value)
            else:
                #once the recursion is broken, we insert the value
                self.left.insert(value)
        else:
            #if the right child is
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        
    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

names_list = BinarySearchTree(names_1[0])

for name in names_1[1:]:
    names_list.insert(name)

duplicates = [] 

for name2 in names_2:
    if names_list.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

"""
# Wrote a little test of the outputs to make sure things weren't off
old_names_way = set('Hallie Vazquez, Peyton Lloyd, Daphne Hamilton, Jaden Hawkins, Dulce Hines, Piper Hamilton, Marisol Morris, Josie Dawson, Giancarlo Warren, Amiah Hobbs, Jaydin Sawyer, Franklin Cooper, Diego Chaney, Carley Gallegos, Ahmad Watts, Malcolm Nelson, Malcolm Tucker, Grace Bridges, Luciana Ford, Davion Arias, Pablo Berg, Jadyn Mays, Marley Rivers, Abel Newman, Sanai Harrison, Cloe Norris, Clay Wilkinson, Salma Meza, Addison Clarke, Nelson Acevedo, Devyn Aguirre, Winston Austin, Carsen Tyler, Hayley Morgan, Aleah Valentine, Camryn Doyle, Josie Cole, Nathalie Little, Leia Foley, Jordin Schneider, Justine Soto, Lennon Hunt, Zara Suarez, Kale Sawyer, William Maldonado, Irvin Krause, Maliyah Serrano, Selah Hansen, Kameron Osborne, Alvaro Robbins, Leon Cochran, Andre Carrillo, Dashawn Green, Eden Howe, Logan Morrow, Ralph Roth, Trace Gates, Megan Porter, Aydan Calderon, Raven Christensen, Ashlee Randall, Victoria Roach, River Johnson, Ali Collier'.split(", "))

new_names_way = set('Ahmad Watts, Franklin Cooper, Jaydin Sawyer, Sanai Harrison, Jaden Hawkins, Cloe Norris, Pablo Berg, Giancarlo Warren, Camryn Doyle, Aleah Valentine, Grace Bridges, Daphne Hamilton, Irvin Krause, Justine Soto, Josie Cole, Winston Austin, Ashlee Randall, Leon Cochran, Kale Sawyer, Alvaro Robbins, Malcolm Tucker, Jadyn Mays, Josie Dawson, Clay Wilkinson, Logan Morrow, Salma Meza, Trace Gates, Hayley Morgan, Dulce Hines, Abel Newman, Nathalie Little, Zara Suarez, Leia Foley, William Maldonado, Marley Rivers, Addison Clarke, Kameron Osborne, Aydan Calderon, Ali Collier, Marisol Morris, Peyton Lloyd, Eden Howe, Victoria Roach, Dashawn Green, Carley Gallegos, Selah Hansen, Hallie Vazquez, Piper Hamilton, Lennon Hunt, Andre Carrillo, Devyn Aguirre, River Johnson, Maliyah Serrano, Diego Chaney, Davion Arias, Nelson Acevedo, Malcolm Nelson, Raven Christensen, Luciana Ford, Amiah Hobbs, Megan Porter, Carsen Tyler, Jordin Schneider, Ralph Roth'.split(", "))
print (len(new_names_way))
print (len(old_names_way))
print (new_names_way == old_names_way) #NB: I had to split on ", " space because the order is different in either list
"""
