
x=[2,3,4]
y=x;


print(y is x); # it will return true because both value oocupy same memory address.y points same memory address as x

a=[1,2,3]
b=[1,2,3]

print(a is b) #it will print false because both a and b both points two different memory location

print(a==b) # it will print true because both objects value is same;

# Example 3: Integers and small strings (interning)
m = 5
n = 5
print(m is n)  # True (Python reuses small integers)
print(m==n)

p = "hello"
q = "hello"
print(p is q)  # True (string interning for small strings)

print(p==q)



print(p==q)