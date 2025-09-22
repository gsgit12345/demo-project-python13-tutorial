class consclassmethod:

    def __init__(h,name,age,rollnum):
        h.name=name
        h.age=age
        h.rollnum=rollnum

    @classmethod
    def assignNameProp(cls,name):
        return cls(name,0,0)          # give default values for missing ones

    @classmethod
    def assignTwoValue(clsd,name,age):
        return clsd(name,age,0)         # give default values for missing ones


    @classmethod
    def assignTHreeVal(cls,name,age,rollnum):
      return cls(name,age,rollnum)      # should return object, not tuple


    @classmethod
    def default(cls):
        print("default const")
d=consclassmethod("name",10,11)

d1=consclassmethod.assignNameProp("harish")

consclassmethod.default()

d0 = consclassmethod("name", 10, 11)
print(d0.__dict__)

d11 = consclassmethod.assignNameProp("harish")
print(d11.__dict__)

d2 = consclassmethod.assignTwoValue("sita", 20)
print(d2.__dict__)

d3 = consclassmethod.assignTHreeVal("ram", 30, 101)
print(d3.__dict__)
