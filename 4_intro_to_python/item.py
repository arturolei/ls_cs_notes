class Item: 
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: {self.price}"

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        # add some data validation.. 
        # is the price a number or not?
        self.name = new_price