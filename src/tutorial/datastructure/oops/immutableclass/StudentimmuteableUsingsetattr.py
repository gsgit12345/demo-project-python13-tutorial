class student:

    def __init__(self,name,age):
       #self.name=name
       #self.age=age   #this will give error because it is calling the __setattr__() to initialize the object
       super().__setattr__("name",name)
       super().__setattr__("age",age)


    def __setattr__(self, key, value):
       raise AttributeError("can not modify attribute ")

st=student("harish",30)

#st.name="ramesh" # immutable object we can not change the state.we have implemented using the setattr()

print(hash(st))



