class Laptop:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
laptop1=Laptop("hp",124,65000)
laptop2=Laptop("dell",164,70000)
print(laptop1.ram)