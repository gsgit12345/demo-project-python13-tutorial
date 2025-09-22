from abc import ABC, abstractmethod


class company(ABC):
    NAME = "Anycompany"
    DATE = "4-4-2025"

    @abstractmethod
    def sayHello(self):
        print(self.NAME )


# c=company() # it will give the error because it is interfcae

class companyImpl(company):
    pass


# im=companyImpl() # it will give the error

class comanyImpl(company):
    def sayHello(self):
        print("implemented in subclass")


impl = comanyImpl()

impl.sayHello()
