x=100

print("before local declaration var:",x)
def  getWindow():
    x=200
    print("in inner variable",x)

getWindow()

print("global var:",x)