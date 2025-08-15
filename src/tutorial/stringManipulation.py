
a='hello'

b=""" hello """  #correct

print(a,b)

c="hello"

print(c)

print("a is memory:",id(a),"b is mempry:",id(b),id(c))

d='''hello
multi'''

print("d is ",d) #it will print hello in first line and multi in second line