class student:

    def printDetail(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
        print("name:",name,"rollnum:",rollnum)


class address(student):
    def  accessPropInChild(self):
        print("name:",self.name,"rollnum:",self.rollnum)

ad=address()
ad.printDetail("ram",1000)  # if you will not call this function  and you will accessPropInChild() it will give
                                            # error because initialization does not happen.in python you can not access property without initialization
ad.accessPropInChild()