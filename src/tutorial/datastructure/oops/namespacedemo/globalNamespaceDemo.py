x=100

def sayHello():
    print("global function")

import types as t
import tutorial.datastructure.oops.moduledemo.calculator as calc

print("t" in globals())

y=100
print("calc" in globals())

print("x" in globals())


print("y" in globals())