
class  student:
    name="harish"
    x=100
    print("name in parent:",name,"x in parent:",x)

class address(student):
    name="rohin"   # here shadowing is happening
    x=200
    print("name in child:",name,"x in child:",x)


#st=student()

#print(st.x,st.name)

