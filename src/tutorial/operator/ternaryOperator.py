age = 18

status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult
# Simple ternary check
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Odd

# Nested ternary (not recommended for readability)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # B


name=20

isVoter="he can vote" if name>18 else "he can not vote"

print(isVoter)

p=10;

++p
print("p is",p," value ")