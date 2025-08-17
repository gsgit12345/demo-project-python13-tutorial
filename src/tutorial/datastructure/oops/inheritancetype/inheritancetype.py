class Animal:
    way="normal barking"
    print("i am animal")
    def bark(self,bark):
        print(self.way,"normal barking in animal")
        print("barking"+bark)
class dog(Animal):
    way="barking barking"
    print("i am in dog class")

    def bark(self,bark):
        print(self.way,"in child class","dog is barking")
        super().bark("barking from child call")


ppp=Animal()

ppp.bark("hello i am barking parent")

doo=dog()
print("===========================")
doo.bark("child")
print("=========================== after assignment")

ppp=doo  # here child class is called

ppp.bark("after assignment")