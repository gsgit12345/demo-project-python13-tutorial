
l=[1,2,3,4,19]

l1=[5,6,7,8,11]


for a,b in zip(l,l1):
      print(":",a,":",b,end=" ")

le=len(l) ;
print()
for a in range(le):
      print(l[a],":",l1[a],end=" ")