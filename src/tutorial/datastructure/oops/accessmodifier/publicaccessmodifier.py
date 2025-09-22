class publicdemo:

    def  sayHello(self,name):   # here name sayHello() function are public
        self.name=name
        print(name)



d=publicdemo()

d.sayHello("ram")  # accessible from outside of class
print(d.name)  # accesible from out side class

