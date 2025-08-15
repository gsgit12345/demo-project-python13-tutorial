
#range()  demo

for i in range(1,9):
    print(i,end=",")

list1=list(["apple","bana","paya","gaya"])
print()
for  item in list1:
    print(item,end=" ")


#using the unpacking
print()

print(*range(1,9),end=" ")

print(*list1,end=" ")
