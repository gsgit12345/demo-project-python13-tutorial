class Amezon:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def printDetail(self):
        print(self.name, self.location)


amx = Amezon("ramkumar", "delhi")

amx.printDetail();

amx = Amezon("raja", "pooja")

amx.printDetail()


class flip(Amezon):

    counter=1
    def __init__(self, name, location):
        super().__init__(name, location)

    def printChild(self):
        print(self.name, self.location)


fl = flip("hello","kusmum")
fl.printChild()

print(fl.counter)