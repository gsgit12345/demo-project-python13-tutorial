from functools import singledispatchmethod
class parser:
    @singledispatchmethod
    def parse(self,data):
        print("unknown format",data)
    @parse.register
    def _(self,data:str):
        if(data.strip().startswith("<")):
            print("xml parser")
        else:
            print("json parser")
    @parse.register
    def _(self,data:bytes):
        print("parsing the by data",data)

p=parser()

p.parse("{")
p.parse(")")
