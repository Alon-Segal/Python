from random import randint
from time import sleep

prize=0
guess=0

list=[]
list.append(randint(1,6))
list.append(randint(7,12))
list.append(randint(13,19))
list.append(randint(20,26))
list.append(randint(27,32))
list.append(randint(33,37))
print("\nWinning numbers: " + str(list))
money=int(input("\nHow much money do you have?: "))

for i in range(money//3):
    print("\nRolling the dice...")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    num1=randint(1,37)
    num2=randint(1,37)
    num3=randint(1,37)
    num4=randint(1,37)
    num5=randint(1,37)
    num6=randint(1,37)
    print("Your numbers are: " + str(num1) + ", " + str(num2) + ", " + str(num3) + ", " + str(num4) + ", " + str(num5) + ", " + str(num6))

    if num1 in list:
        guess=guess+1
        print(str(num1) + " is inside")
    elif num2 in list:
        guess=guess+1
        print(str(num2) + " is inside")
    elif num3 in list:
        guess=guess+1
        print(str(num3) + " is inside")
    elif num4 in list:
        guess=guess+1
        print(str(num4) + " is inside")
    elif num5 in list:
        guess=guess+1
        print(str(num5) + " is inside")
    elif num6 in list:
        guess=guess+1
        print(str(num6) + " is inside")
    else:
        print("\nNo match")

if guess==6:
    prize=prize+1000000
    print("You won " + str(prize) + " ILS!!!")
elif guess==5:
    prize=prize+5000
    print("You won " + str(prize) + " ILS!!")
elif guess==4:
    prize=prize+100
    print("You won " + str(prize) + " ILS!")
elif guess==3:
    prize=prize+10
    print("You won " + str(prize) + " ILS")

else:
    print("\nYou didn't win this time...")

print("Total good numbers: " + str(guess))
print("Your total prize: " + str(prize) + " ILS")

