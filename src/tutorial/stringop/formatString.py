student = {
    "name": "hello",
    "age": 123
}

print(f"hello name {student['name']} and age {student['age']}")


text="hello java {fnam} and i am here {delhi}".format(fnam="ghanshyam",delhi="cahe here")

print(text)

text1="my age is {} and place is {}".format("32","delhi")

print(text1)

text3=f"my age is {student['age']} and name is {student['name']}";

print((text3))

text4="hello i am in {a:10}".format(a=10)  # craeting the space.10 space created but 2 is occupied by 1 and 0.8 space u can find

print(text4)