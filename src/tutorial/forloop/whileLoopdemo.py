counter = 1

while counter < 9:
    print(counter, end=" ")
    counter += 1
print()
guess = None

secret = 9

while guess != secret:

    guess = int(input(print("enter the numebr")))
    if (guess < secret):
        print("gues is too low")
    elif (guess > secret):
        print("too high")
    else:
        print("hello")
