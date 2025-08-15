student={
    "name":"ram",
    "age":123,
    "email":"demo@gmail.com"
}

print(student)

for i in student:
    print(i)
    print(student[i])


name=dict(name="ram",age=123,id=1234)   #using constructor

print(name)

# using the tuples

addr=dict([("name","ram"),("emai","hello@gmail.com"),("zip",1234),("city","delhi")]) # this is using the tupple

print(addr)

# using the zip function

key={"name","age","id","email"}
value={"harish",123,23,"hello@gmail.com"}

mydic=dict(zip(key,value))
print("below is my dict")
print(mydic)


