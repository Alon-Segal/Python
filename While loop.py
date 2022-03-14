while(True):
    name=input("Enter a name: ")
    if(name=="idan"):
        print("Hello idan")

    elif(name=="ben"):
        print("Hello ben")

    else:
        print("I don't know you..")

    exit=input("\nDo you want to want to exit? y/n\n")
    if (exit=="y"):
        break
    elif (exit=="n"):
        continue
    else:
        print("Choose y/n only!")

print("Bye bye...")