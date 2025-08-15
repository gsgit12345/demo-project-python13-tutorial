def sayHello(*x):
    print("n number of argument",x)


sayHello(1,2,3,4,5,6,7)


t=tuple([1,2,3,4,5])

print(t)

sayHello(*t)