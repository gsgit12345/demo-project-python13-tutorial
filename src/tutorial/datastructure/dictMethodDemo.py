
student={
    "name":"ram",
    "age":1224,
    "email":"demo@gmail.com",
    "stid":12345,
    "addr":"delhi"
}


#items()
for  a,b  in student.items():
    print("key:",a,"value:",b)

# get  demo

for a in student:
      print("get demo",student.get(a)) # it will print the value

del student["name"];

print(student)
