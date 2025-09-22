class  privatepropertydemo:

    def __sayHello(self,name):
        self.__name=name


    def   display(self):
        self.__sayHello()

class  childcls(privatepropertydemo):

    def  displayProp(self):
        self.__sayHello()


pr=childcls()

#pr.__sayHello()  # hello is the private function . we can not access

#print((pr.__name))   # private property .can not access __name

