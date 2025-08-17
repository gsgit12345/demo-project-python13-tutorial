def getDepartment():
    name="payment"
    pin="123345"
    print("name is:"+name+":pin:"+pin)
    def location():
        nonlocal  name
        name="hr department"
        print("in inner:"+name)
    location()
    print("printing after changing:"+name) #here name's value has been change

getDepartment()
