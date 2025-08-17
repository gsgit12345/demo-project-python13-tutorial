def sayHello():
    x=100
    print("after x")
    k=20


print("x" in locals())

print("k" in locals())


def printEmployee():
    name = "ramesh kumar"
    print(name, locals())
    print("name" in globals())

    def printAdress():
        nonlocal name     # just declare nonlocal
        name = "hello"    # assign in next line
        pin = "1233"
        print(pin)
        print(locals())
        print("outer variable", "name" in locals())
        name = "changing the value of outer"
        print(name)

    printAdress()
    print("After changing:", name)

printEmployee()
