class Car:
    wheels = 4   # class attribute

    def __init__(self, brand):
        self.brand = brand   # instance attribute

    def show(self):   # instance method
        print("Brand:", self.brand, "Wheels:", self.wheels)

c1 = Car("Tata")
c1.show()   # Brand: Tata Wheels: 4

c2 = Car("bata")
c2.show()   # Brand: Tata Wheels: 4
