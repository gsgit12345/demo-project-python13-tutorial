from abc import ABC,abstractmethod

class  PhoneInterface(ABC):   #this is the interface
    @abstractmethod
    def sayHello(self):    #abstract method in interface
        pass
    def  barking(self):   # this is the empty method
        pass


class Nokiya(PhoneInterface):
    def sayHello(self):
        print("i am inherited from the phoneinterface")

n=Nokiya()
n.sayHello()


# 🔹 Why no error?
#
# Because:
# PhoneInterface had only one abstract method (sayHello).
# Nokiya overrides it.
# Therefore, Nokiya satisfies the abstract contract → it’s a concrete class.
# The method barking in PhoneInterface is NOT abstract (it has no @abstractmethod), so overriding it is optional.
