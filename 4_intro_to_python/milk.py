from item import Item

class Milk(Item):
    def __init__(self, name, price, milk_type, expiration_date):
       super().__init__(name,price)
       self.milk_type = milk_type
       self.expiration_date = expiration_date  

    def __str__(self):
        return f"{super().__str__()} type: {self.milk_type} expires on {self.expiration_date}"