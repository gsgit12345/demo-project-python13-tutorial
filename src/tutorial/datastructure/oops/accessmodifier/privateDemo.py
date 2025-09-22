class privateDemo:
    __version="123"
    def __sayHello(self,name):   # this is the private method.can not access from outside
        self.__name=name         # __name is private and can not access from outside
        print(self.__name)
    def  detail(self):
        self.__sayHello("ramesh")  # but we can access within class


dd=privateDemo()

dd.detail()
#dd.__sayHello()  # can not access ouside of the class

#print(privateDemo.__version) # can not access because class properrty version is private