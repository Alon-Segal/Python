# display the current date and time
# from datetime import datetime
# print("Current date and time: " + str(datetime.now()))


# accepts the user's first and last name and print them in reverse order with a space between them
# name=input("Enter first name: ")
# last_name=input("Enter last name: ")
# print(name[::-1] + " " + last_name[::-1])
# a=name + " " + last_name
# b=' '.join(a[::-1])
# print(b)


# accept a filename from the user and print the extension of that
# filename=input("Enter a file name: ")
# f_extns=filename.split(".")
# print(repr(f_extns[-1]))


# find whether a given number is even or odd
# num=int(input("Enter a number: "))
# if(num%2==0):
#    print("This is an even number")
# else:
#    print("This is an odd number")


# convert height in feet and inches to centimeters
# print("Input your height: ")
# h_ft = int(input("Feet: "))
# h_inch = int(input("Inches: "))
# h_inch += h_ft * 12
# h_cm = round(h_inch * 2.54, 1)
# print("Your height is : %d cm." % h_cm)


# empty a variable without destroying it
# n=20
# d={"x":200}
# l=[1,3,5]
# print(type(n)())
# print(type(d)())
# print(type(l)())


# add a key to a dictionary
# new_dictionary={0:10,1:20}
# print(new_dictionary)
# new_dictionary.update({2:30})
# print(new_dictionary)


# create a dictionary from a string, track the count of the letters from the string
from collections import defaultdict, Counter
# s = "Net4U"
# new_dict = {}
# for letter in s:
#    new_dict[letter] = new_dict.get(letter, 1)
# print(new_dict)


# get a single string from two given strings, separated by a space and swap the first two characters of each string
# a="abc"
# b="xyz"
# new_a=b[:2] + a[2:]
# new_b=a[:2] + b[2:]
# print(new_a + " " + new_b)


# count repeated characters in a string
# import collections
# a="thequickbrownfoxjumpsoverthelazydog"
# b=collections.defaultdict(int)
# for c in a:
#    b[c] += 1
# for c in sorted(b, key=b.get, reverse=True):
#    if b[c] > 1:
#        print('%s %d' % (c, b[c]))


# sum all the items in a list
# list1=[1,2,3,4,5,6,7,8]
# sum=0
# for i in range(len(list1)):
#    sum=sum+list1[i]
# print("Summary: ", sum)


# print a specified list after removing the 0th,4th and 5th elements.
# list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# list1.pop(5)
# list1.pop(4)
# list1.pop(0)
# print(list1)

# accept an integer (n) and compute the value of n+nn+nnn
# n=int(input("Enter a number : "))
# print(n + (n*10+n) + (n*100+(n*10)+n))
