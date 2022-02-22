from random import randint
from time import sleep

money=int(input("\nWelcome to the cube game\nprice - 3$ per turn \n\nEnter amount of money to play: "))
if (money>=3):
    print("\nyou have: " + str(money//3) + " turns\nYour change is: " + str(money%3))
else:
    print("\nYou don't have enough money to play...")

prize=0

for i in range(money//3):
    print("Rolling the dice...")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    num1=randint(1,6)
    num2=randint(1,6)
    print("Cube 1: " + str(num1) + "\nCube2: " + str(num2))

    if (num1==num2):
        if (num1==6==num2==6):
            prize=prize+1000
            print("\nYou won 1000$\n")
        else:
            prize=prize+100
            print("\nYou won 100$\n")
    elif (num2==2):
        prize=prize+40
        print("\nYou won 40$\n")
    elif (num1==1):
        prize=prize+20
        print("\nYou won 20$\n")
    else:
        print("\nYou didn't win this time...")


print("Your prize: " + str(prize) + " $")