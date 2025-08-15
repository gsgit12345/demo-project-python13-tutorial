lst=[1,2,3,4,5,5,6,7]

for i in lst:
    print(i,end=" ")

len1=len(lst)
print()
for j in range(len1):
    print(j,end=" ")

print()
#reversing a list
for n in range(len1-1,-1,-1) :
    print(n,end=" ")
print()
m=[n for n in range(1,101) if n%2==0 ]

print(m)

lst11 = [x for x in range(1,4) ]
print(lst11)
lst12=[y for y in range(3,0,-1)]
print(lst12)



lst1 = [x*y for x in range(1,4) for y in range(3,0,-1)]
print(lst1)
# [1, 2, 3] *
# [3, 2, 1]
# This is a nested loop in list comprehension.
#
# Multiplying each x in [1,2,3] with each y in [3,2,1]
#
# Output: [3, 2, 1, 6, 4, 2, 9, 6, 3]


lst3 = [x for x in range(10) if x%2 == 0 if x > 5]
print(lst3)

words1 = ["apple", "banana", "cherry"]
lst21 = [w[0].upper() for w in words1 if "a" in w]
print(lst21)

lstt = [[j for j in range(i)] for i in range(4)]
print(lstt)
lstc = [x if x%2==0 else -x for x in range(5)]
print(lstc)
