class instancemethod:
    def __init__(self,name):
        self.name=name


    def instancemethod(self):
        print(self.name)


instanced=instancemethod("ram")

instanced.instancemethod()