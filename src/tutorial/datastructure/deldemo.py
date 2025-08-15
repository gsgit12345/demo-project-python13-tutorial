person={
    "name":"harish",
    "age":12345,
    "city":"delhi",
    "skills":["java","python"],
    "married":True

}

for  a in ["name","age"]:
   del person[a]
   print(person)

del person["skills"]

print((person))