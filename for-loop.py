from time import sleep

#print 1-100 hop every 2 numbers
for x in range(1,100,2):
    print(x)
    sleep(0.1)

#Get multiple inputs 5 times
print("\nNow we will get all the details about your class\n")
for i in range(1,5):
   name=input("Enter a name: ")
   last=input("Enter last name: ")
   age=int(input("Enter an age: "))
   phone=input("Enter a phone number: ")
   print("\nPrinting student number " + str(i) + " information...\n")
   sleep(3)
   print("Full name: " + name + "\nLast name: " + last + "\nAge: " + str(age) + "\nPhone: " + phone + "\n")
   sleep(1)