from datetime import datetime
x = 5
y = 10

print(f"Sum: {x + y}")              # Output: Sum: 15
print(f"Upper: {'python'.upper()}") # Output: Upper: PYTHON


num=234.1234

print(f"num:{num:.2f}")

date="2024/08/2"

now =datetime.now();

print(f"date:{now:%y-%m-%d}")