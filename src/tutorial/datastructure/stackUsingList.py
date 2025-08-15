stack = []

while True:
    choice = int(input('''
            1-add element in stack
            2-Pop Element from statck
            3-dlete element from stack
            4-display stack
             5-exit 
                '''))
    if   choice == 1:
           k = input("enter the value to append")
           stack.append(k)
    elif choice == 2:

            v=stack.pop()
            print(v)
            print(stack)
    elif choice==3 :
            n=input("enter value to be delete")
            stack.remove(n)
    elif choice==4:
             print(stack)
    else:
       break;


