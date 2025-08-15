a="hello i "

lenth= len(a);


for  i in  a :
    print(i,end=" ")

print()
for i in range(0,lenth):
    print(a[i],end="")


print()

for i in range(lenth-1,-1,-1):
    print(a[i],end=" ")

# reverse string using slice method

print()
print(a[::-1])