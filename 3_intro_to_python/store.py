class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories 

    def __str__(self):
        store_string = self.name
        i = 1
        for category in self.categories:
            store_string += f"\n{i}. {category}"
            i+=1

        return store_string
    

my_store = Store("Moe's Groceries", ['alcohol', 'dynamite', 'cough syrup'])

print(my_store)
selection = ""
while selection is not "q":
    selection = input(f"Please input a number between 1 and {len(my_store.categories)} or 'q' to quit: ")
    print(f"User selected {selection}")


