d = {"a": 1, "b": 2}
print(d.pop("c", None))

d = {"x": 100}
#print(d.pop("y")) # it will give error because key does not exist

d = {"a": 1, "b": 2, "c": 3}

for a in d.keys():
    if a=="c":
        d.pop(a)
        print(d)
