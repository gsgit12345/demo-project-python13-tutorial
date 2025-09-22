class coder:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __eq__(self, other):
        if isinstance(other,coder):
            return self.age==other.age and self.name==other.name
        return False
code=coder("harish",100)
code1=coder("harish",100)

if code==code1:
    print("both object are equal")
else:
  print("object content is not equal")

print(code)

print(code1)