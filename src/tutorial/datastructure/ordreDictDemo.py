from   collections import OrderedDict



orddict=OrderedDict(name="ram",age=123,email="xyz@gmail.com")

print(orddict)

names={"ram","kumar","shukla"}
title={"fname","miname","lname"}

nameod=OrderedDict(zip(title,names)) #does not preserve because  names and title are set

print(nameod)


od=OrderedDict()
od['name'] = 'John'
od['age'] = 30
od['city'] = 'New York'
print(od)

#  we can also create from the normal dict
