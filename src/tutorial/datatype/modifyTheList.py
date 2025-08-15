
list=["helo","kl","ert"]


list.append(34)

list.extend([45,90])

print(list)

list.insert(3,"how")

print(list)


#delete operation


print("rmovr",list.remove(45))

print(list)

# some more operation

list=[1,12,13,14,45,16,74,81]
list.pop()   # it removes the last element
print(list)


list.pop(1)

print(list)
list=[1,12,13,14,45,16,74,81]

del list[4]

print(list)


