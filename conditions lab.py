choice=input("\nMenu:\n1.Insert a number and ** it by 3\n2.Insert 4 IPs to a list and print it\n"
        "3.Insert 4 Entries to DNS_Dictionary and print it\n4.Check if a word is Polindrom\n\nSelect 1-4:\n")

if(choice=="1"):
    num1=input("Insert a number: ")
    num2=(int(num1)**3)
    print("\nYour number: " + str(num1) + "**3 = " + str(num2))

elif(choice=="2"):
    ip_list=[]
    ip_list.append(input("Insert IP - 1: "))
    ip_list.append(input("Insert IP - 2: "))
    ip_list.append(input("Insert IP - 3: "))
    ip_list.append(input("Insert IP - 4: "))
    print("Your IP: " + str(ip_list))

elif(choice=="3"):
    DNS_Dictionary={}
    DNS_Dictionary.update({input("Insert a first URL: "): input("Enter a first IP")})
    DNS_Dictionary.update({input("Insert a 2nd URL: "): input("Enter a 2nd IP")})
    DNS_Dictionary.update({input("Insert a 3rd URL: "): input("Enter a 3rd IP")})
    DNS_Dictionary.update({input("Insert a 4th URL: "): input("Enter a 4th IP")})
    print("\nDNS_Dictionary: " + str(DNS_Dictionary))

elif(choice=="4"):
    word=input("Enter a word: ")
    if (word == word[::-1]):
        print("\nThis word is polindrom")
    else:
        print("\nThis word is not polindrom")
else:
    print("Please select 1-4 only")