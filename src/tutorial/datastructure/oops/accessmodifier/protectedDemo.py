class protecteddemo:

    def sayHello(self,name):
        self._name=name     # _name is protected but still you can access from outside of the class
        print(name)

    def _showDetail(self):
        print(self._name)

pr=protecteddemo()

pr.sayHello("harish")

print(pr._name)  # accessible from out side but _name is protected and _showDetail() is also protected

pr._showDetail()