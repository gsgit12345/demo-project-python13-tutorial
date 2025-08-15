from types import  MappingProxyType

a={"a":"shyam","b":100,"c":"sd@mailid"}

prxdict=MappingProxyType(a)

print(prxdict)
#prxdict[a]="harish" # it will give the error because you can not modify in dict

a["a"]="harsh"

print(prxdict)
