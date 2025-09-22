from dataclasses import dataclass

@dataclass
class student:

    name:str
    age:int




s=student("harish",100)

s.name="mukesh" #you are to change

print(s)


@dataclass(frozen=True)
class Place:
    name:str
    pin:int


p=Place("delhi",100)


print(p)

#p.name="hyderabasd" #you can not assign a value