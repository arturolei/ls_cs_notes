from item import Item

class Category:
    def __init__(self, name, items = []):
        self.name = name
        self.items = items
    
    def __str__(self):
        output = f"{self.name} contains items: "
        for item in self.items:
            output += f"\n {item.get_name()} "
        return output
    
    def get_name(self):
        return self.name 
    
    def set_name(self, new_name):
        self.name = new_name
  
  #Category and Item.py---Has a --> Composition Things are contained by other things