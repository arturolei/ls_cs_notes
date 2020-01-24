from category import Category
from item import Item
from milk import Milk

class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories #item that we have is an attribute in the containing class

    def __str__(self):
        store_string = self.name
        i = 1
        for category in self.categories:
            store_string += f"\n{i}. {category.get_name()}" 
            i+=1

        return store_string
    
    def get_name(self): #setter of self
        return self.name 
    
    def set_name(self, new_name):
        # Here is where we might want to install controls 
        # to monitor inputs, especially if we have non-ideal data types
        self.name = new_name 
        
        # Why do we not let other person do instance.name = "new Name"? 
        # ENCAPSULATION: PRotec our data, let's not have a class overwrite another
        # LOSING CONTROL, setter can block unintended input

    # We often need a getter and setter for all attributes
    def get_categories(self):
        return self.categories 
    
    def set_categories(self, new_categories):
        self.categories = new_categories
    

my_store = Store("Moe's Groceries", 
                [Category('alcohol', [Item("Bourbon", 100), Item("Vodka", 50)]), Category('matches', [Item('Flint', 2)]), Category('cough syrup', [Milk('Cowgirl Creamery', 300, "Whole", 20200131)])])

print(my_store)
selection = ""
while selection is not "q":
    selection = input(f"Please input a number between 1 and {len(my_store.categories)} or 'q' to quit: ")
    if selection is not "q":
        print(f"User selected {selection}")
        print(my_store.get_categories()[int(selection)-1])


## Task:
## Build an interactive store that when opened,
# displays a name and all shopping categories. 
# Users can enter a number to select a specific category 
# which should display more detailed info (inventory) 
#
##

## Inputs/Outputs: Nouns
## Actions: Verbs

# Why use getters and setters at all? Encapsulation --> 


## Aggregation/Composition--> Very similar 
# Composition/Association/Aggregation