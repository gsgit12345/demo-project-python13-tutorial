class student:
    name="hello"
    @classmethod
    def getstudent(cls):

        print(cls.name)



st=student()
st1=student()

st.name="parse"
st1.name="xyb"
print(st.name)

print(st1.name)