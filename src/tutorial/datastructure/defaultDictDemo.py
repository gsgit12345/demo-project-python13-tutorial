from collections import defaultdict


di=defaultdict(int)

print(di["a"])

d = {}
#print(d["a"])  # ❌ KeyError


def someValue():
    a=8
    b=10
    return a*b

dic=defaultdict(someValue)   # in the same way you can put int,set,list eyc

print(dic["miss"])

#Using a Lambda Function
dd = defaultdict(lambda: "Unknown")
print(dd["city"])  # Unknown
