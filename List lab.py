new_list=["James", 25, "James@gmail.com", "050000000"]
print("\nMy name: " + new_list[0] + "\nAge: " + str(new_list[1]) + "\nMail: " + new_list[2] + "\nPhone: " + new_list[3])

new_list1=["192.168.1.1", "192.168.1.255"]
print(new_list1)
new_list1.append("192.168.1.10")
new_list1.append("192.168.1.20")
new_list1.append("192.168.1.30")
print(new_list1)

new_list1.pop(2)
print(new_list1)

print("\nLength: " + str(len(new_list1)) + "\nIP list: " + str(new_list1))