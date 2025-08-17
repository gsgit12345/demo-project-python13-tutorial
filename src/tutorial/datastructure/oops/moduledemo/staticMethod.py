class   employee :
    @staticmethod
    def calculateSal(a):
        print("i am in static method")
        d=a*a+100
        return d

    @classmethod
    def getDetail(cls,detail):
        print("this is the class method")
        return detail

    def normalFunction(self,de):
       print("this is the normal function")


emp=employee()

hello=emp.normalFunction("this normal function")

print(hello)

clsmeth=employee.getDetail("detail is")
print(clsmeth)

emp.getDetail("")

