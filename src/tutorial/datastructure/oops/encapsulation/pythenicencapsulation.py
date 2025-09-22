class  pythenicencapsulation:
    def  __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def  name(self):
       return  self._name    #this is the getter in python
    @name.setter
    def setName(self,name):
        self._name=name

    @property
    def age(self):
        return self._age

    @age.setter
    def setAge(self,age):
        self._age=age;


dd=pythenicencapsulation("harish",100)

print(dd.age)