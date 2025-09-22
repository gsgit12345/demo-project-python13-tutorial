class  Area:

    def __init__(self,name):   #this is the single parameter constructor
        self.name=name

a=Area("delhi")

b=Area("delhi")

print(a.name,b.name)

b.name="hyd"

print(a.name,b.name)
