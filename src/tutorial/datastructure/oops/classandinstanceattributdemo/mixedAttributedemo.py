class Pincode:
    pin="12345"

    def __init__(self,name,location,pin):

        self.name=name
        self.location=location
        self.pin=pin


p=Pincode("delhi","sagarpur","1234")

p1=Pincode("delhi","uttam","321")


print((p.name,p.location,p.pin))

print((p1.name,p1.location,p1.pin))

Pincode.pin=7890

print((p1.name,p1.location,p1.pin))
print((p.name,p.location,p.pin))
