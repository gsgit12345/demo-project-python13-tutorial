tpt=tuple(("name","harish","suresh"))

print(tpt)

#tpt1=tuple(20)  # this element is not tuple

#print(type(tpt1))  # int is not iterable that is why it is giving error

tpt2=tuple("20")

print(type(tpt2))  # int is not iterable that is why it is giving error


# nested tuple


t3 = tuple((1, tuple((2, 3))))

print(t3)

t4=tuple((20,tuple((2,30,tuple((40,50))))))

print(t4)


t5=tuple((34,50,tuple((409,90,tuple((12,0))))))

print(t5)


t7=(34,(45,(60,(10,(35)))))

print(t7)


t6=tuple((100,1,4,tuple((23,0,tuple((300,80,tuple((24,80,tuple((49,))))))))))

print("t6 is:",t6[3][2][2])


#nested tuple

t9=(34,(40,(50,(100,(45,(1000,(300,)))))))

print(t9[1][1])


t2 = ("apple",)
print(type(t2))   # <class 'str'>

# tuple from string

s="hello"
t10=tuple(s)

print(t10)  #it will print (h,e,l....)

t = ("hello", "world")
result = " ".join(t)
print(result)  # hello world



