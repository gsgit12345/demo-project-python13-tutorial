class varargsconst:

    def __init__(self,*param):
        if len(param)==0:
            self.name="unknown"
            self.age=0
            self.addr=""
            self.id=""
        elif len(param)==1:
            self.name=param[0]
            self.age=0
            self.addr=""
            self.id=""
        elif len(param)==2:
            self.name=param[0]
            self.age=param[1]
            self.addr=""
            self.id=""
        elif len(param)==3 :
            self.name=param[0]
            self.age=param[1]
            self.addr=param[2]
            self.id=""
        elif len(param)==4:
            self.name=param[0]
            self.age=param[1]
            self.addr=param[2]
            self.id=param[3]
        else:
          print("exceeded parameter")
    def  dispaly(self):
         print(self.id,self.name,self.addr,self.age)

de=varargsconst()
de.dispaly()

de=varargsconst("harish")
de.dispaly()

de=varargsconst("harish",100) # in this way we can overload
de.dispaly()