class Animal:

    def _bark(self,type): # here _bark is proteced and _type is also protected
        self._type=type


class  dog(Animal):
    def barking(self):
        print(self._type)
        self._bark("hello")


d=dog()
d._bark("kohili") # we can access using child object

d.barking()