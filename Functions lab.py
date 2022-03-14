from random import randint
from time import sleep

def menu():
    while(True):
        choice=input("Menu:\n1.Dog's details\n2.Friends list\n3.N Azzeret\n")
        if(choice=="1"):
            Dogs()
        elif(choice=="2"):
            Friends()
        elif(choice=="3"):
            Azzeret()
        else:
            print("Enter 1-3 only!!\m")
            continue
        exit=input("Do you want to exit? y/n\n")
        if(exit=="y"):
            break
        else:
            print("Welcome back\n")
    print("Bye bye")

def Dogs():
    name=input("Enter dog's name: ")
    age=int(input("Enter dog's age: "))
    print("\nDog's name: " + name + "\nDog's age: " + str(age*7) + "\n")

def Friends():
    list_friends=[]
    for i in range(5):
        list_friends.append(input("Enter a friend's name: "))
    name=input("Enter a new name: ")
    if(name in list_friends):
        print(name + " is inside the list!\n")
    else:
        print(name + " isn't inside the list\n")

def Azzeret():
    num=int(input("Enter a number: "))
    sum=1
    for i in range(1,num+1):
        sum=sum*i
    print(str(num) + " Azzeret is: " + str(sum) + "\n")

menu()