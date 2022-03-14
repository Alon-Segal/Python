from time import sleep
from random import randint
while True:
    choice=input("\nMenu:\n1.Printing 100 numbers\n2.Check fibo\n3.Randint numbers until we get 12 or we count 10 times")
    num=0
    if choice=="1":
        for i in range(100):
            num=num+1
            print(num)
            sleep(0.05)
            if (num==100):
                break

    elif choice=="2":
        fibo=[1,2,3,5,8,13,21,34,55,89]
        for i in range(2, len(fibo)):
         print(fibo[i])
         print(fibo[i-1])
         print(fibo[i-2])
         print("\n")
        if fibo[i]!=fibo[i-1]+fibo[i-2]:
                print("This is not a fibo\n")
        else:
                print("This is a fibo\n")

    elif choice=="3":
        counter=1
        num=randint(1,12)
        while(num!=12 and counter<11):
            print("Counter: " + str(counter) + " Number: " + str(num))
            counter=counter+1
            num=randint(1,12)
            if (num==12 or counter==10):
                print("Counter: " + str(counter) + " Number: " + str(num))
                break

    exit=input("\nDo you want to exit? y/n\n")
    if exit=="y":
        break

print("\nBye bye..")