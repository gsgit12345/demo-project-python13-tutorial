person ={
    "name":"harish",
    "age":1234,
    "city":"delhi"


}


key=["name","age","city","gender"]

for a in key:
     value=person.get(a,"avaiableornot")
     print(f"{a}:{value}")

print(person.get("gender","name"))


