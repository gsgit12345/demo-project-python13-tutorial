from functools import singledispatch

@singledispatch
def sayHello(a):
    print("first function")

@sayHello.register(int)
def _(data):
    print("int version of function",data)

@sayHello.register(str)
def _(data):
    print("str version of function",data)

@sayHello.register(tuple)
def _(data):
    print("tuple version of function",data)


sayHello(12)