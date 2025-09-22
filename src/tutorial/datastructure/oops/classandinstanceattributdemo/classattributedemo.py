class Department:
    name:str



d=Department()

d1=Department()

Department.name="hr"

print(d1.name)
print(d.name)

d.name="hello"

print(d1.name)
print(d.name)

# Execution flow
#
# Department.name = "hr"
# → This creates a class attribute called name.
# Now Department.name == "hr".
#
# print(d1.name)
# → Python looks in d1 (the instance). No name there.
# → Falls back to the class → finds Department.name = "hr".
# ✅ Output: hr.
#
# print(d.name)
# → Same reasoning as above.
# ✅ Output: hr.
#
# d.name = "hello"
# → This creates an instance attribute name on d only.
# → Now d.name = "hello", but Department.name is still "hr".
# → d1.name still sees "hr" from the class.
#
# print(d1.name)
# → No instance attribute, so still goes to the class.
# ✅ Output: hr.
#
# print(d.name)
# → Finds the instance attribute name="hello".
# ✅ Output: hello.