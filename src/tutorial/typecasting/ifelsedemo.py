

a = int(input("Enter the marks: "))

if a >= 60:
    print("First division")
elif a >= 45:
    print("Second division")
else:
    print("Failed")


temperature = int(input("Enter temperature in °C: "))

if temperature < 10:
        print("Wear a jacket and scarf.")
elif temperature < 20:
        print("Wear a sweater.")
elif temperature < 30:
        print("Wear light clothes.")
else:
    print("It's too hot, stay hydrated!")
