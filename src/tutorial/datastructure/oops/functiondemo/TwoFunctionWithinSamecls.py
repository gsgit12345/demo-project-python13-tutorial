class Parser:
    def parse(self,xml):
        print("parsing xml file")

    def parse(self,json):       #  it is overriding silently previous method
        print("parsing json file")


par=Parser()

par.parse("xml")