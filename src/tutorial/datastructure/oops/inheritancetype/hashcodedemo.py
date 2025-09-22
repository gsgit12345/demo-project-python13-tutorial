class place:
    def __init__(self,pin,name):
        self.name=name
        self.pin=pin
    def __hash__(self):
        return hash((self.name,self.pin))  #pass here tuple  and thsi robust hash implementation

p=place(1001,"delhi")

p1=place(1001,"delhi")

print(hash(p))

print(hash(p1))