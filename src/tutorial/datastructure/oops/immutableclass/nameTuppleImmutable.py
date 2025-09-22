from collections import namedtuple

Student=namedtuple("Student",["roll","age"]) # this is one way.List of strings

st=Student("1awe33",100)

print(st.roll)

print(st.age)


Animal=namedtuple("Animal","height,type") # this is second way

an=Animal(12,"wild")

print(an.height)

print(an.type)


Boy=namedtuple("Boy","height type") # this is third  way

b=Boy(12,"wild")

print(b.height)

print(b.type)

c = b._replace(type=30)  #here   c is the new object.not we changong in currecnt opject.c is the tupple

d=c._asdict() #d is here dict

print("d is",d)

print(b._fields)

data = ["R102", 22]
st3 = Student._make(data)
print(st3)



print(c)
