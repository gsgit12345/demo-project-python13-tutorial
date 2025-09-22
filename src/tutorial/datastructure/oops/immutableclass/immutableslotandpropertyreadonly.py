class Animal:
    __slots__=("_roll","_age")

    def  __init__(self,roll,age):
        self._roll=roll
        self._age=age

    @property
    def getroll(self):
        return self.roll
    @property
    def getage(self):
        return self.age


an=Animal(100,20)

print(an.age,an.roll)