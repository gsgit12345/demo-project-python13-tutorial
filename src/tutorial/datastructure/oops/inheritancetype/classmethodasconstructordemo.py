class  pay:
    @classmethod
    def getObject(cls,name,age):
        cl=cls()
        cl.name=name
        cl.age=age
        return cl


    def dispalyOb(self):
        print(self.name,self.age)

p=pay.getObject("raheem",100)


p.dispalyOb()