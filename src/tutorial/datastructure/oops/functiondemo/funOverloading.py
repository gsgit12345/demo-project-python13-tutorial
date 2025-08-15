def  sayHello(a):
    print(a)
    print("single param")


def sayHello(a,b):    #it overrides previous function
    print(a,b)
    print("double param")



#sayHello(10) does not works

sayHello(10,10)  # it works