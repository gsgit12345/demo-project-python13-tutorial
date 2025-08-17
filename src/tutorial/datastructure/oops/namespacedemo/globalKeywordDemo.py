x=100


def globalKewordDemo():
    x=19000  # overriding global variable in function
    print(x)

#globalKewordDemo()

print(x)   #  global variable of function


def changetheGlobal():
    global x
    x=1000
    print("aftre changing :",x)

#changetheGlobal()

print("change reflected in x after function scope:",x)

if __name__ =="__main__":
  print("x value in module:",x)
  globalKewordDemo()
  changetheGlobal()

