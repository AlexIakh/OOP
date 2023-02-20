class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Tun validations to the recieved argumentes
        assert price >= 0, f"Price is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity is not greater or equal to zero!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
item1 = Item("Phone", 800, 1)
item2 = Item("Laptop", 1000, 5)


print(item1.calculate_total_price())
print(item2.calculate_total_price())
