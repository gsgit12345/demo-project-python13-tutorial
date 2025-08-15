def sayHello(**a):
    print(a)



sayHello(name="harish",age=123,mailid="hello2gmail.com")

b={'name': 'harish', 'age': 123, 'mailid': 'hello2gmail.com'}

sayHello(**b)  #from dictionary and pasing dictinary using unpacking

