import random

list1=["rock","paper","scissor"]


while True:
    ucount=0
    ccount=0
    uc=int(input('''
    
    game started  .........
    1 yes
    2 no | exit
    '''))
    if uc==1:
           for a in range(1,6):
               userin=int(input('''
               1 rock
               2 paper
               3 scissor
               '''))
               if userin==1:
                   choice="rock"
               elif userin==2:
                   choice="paper"
               elif userin==3:
                   choice="scissor"
               comchoice=random.choice(list1)
               if choice==comchoice:
                   print("computer choice",comchoice)
                   print("user choice ",choice)
                   print("game draw")
                   ucount=ucount+1
                   ccount=ccount+1
               elif (choice=="rock" and comchoice=="scissor") or (choice=="paper" and comchoice=="rock") or (choice=="scissor" and comchoice=="paper"):
                   print("computer choice",comchoice)
                   print("user choice ",choice)
                   print("u win")
                   ucount=ucount+1
               else:
                   print("computer choice",comchoice)
                   print("user choice ",choice)
                   print("computer draw")
                   ucount=ucount+1
                   ccount=ccount+1



    else:
         break;


