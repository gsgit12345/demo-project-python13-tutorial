class  location:

    def __new__(cls, *args, **kwargs):
        print("creating the object ")

        obj=super().__new__(cls)
        print(type(obj))
        return obj;
        print("hello") # there is no compile time error and it will not give any error
#print("aftre class")  # it will compile time error. due to indentation
    def  __init__(self,name,location):
        self.name=name
        self.location=location
    def __str__(self):
        return f"(loc={self.location} and name={self.name})"
    def __repr__(self):
        return f"student({self.location},{self.name})"

loc=location("raheem","suresh")

print(loc)

print(repr(loc))