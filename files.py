#r - read only
#w - overwrite on a file
#a - append/add to a file
#r+ - read and overwrite


###How to print specific lines of a file
#filename="C:/Users/Alon/Desktop/python.txt"
#file=open(filename, "r")
#print(file.readlines()[0])
#file.close()

###Full file read
#filename="C:/Users/Alon/Desktop/pythontest.txt"
#file=open(filename, "r")
#print(file.read())
#file.close()

###Read file as list
#filename="C:/Users/Alon/Desktop/pythontest.txt"
#file=open(filename, "r")
#print(file.readlines())
#file.close()

###How to create a new file
#file=open("C:/Users/Alon/Desktop/hello6.txt", "x")
#file.close()

###How to write to a file - r+ / a / w
#filename="C:/Users/Alon/Desktop/pythontest.txt"
#file=open(filename, "r+")
#print(file.read())  #only r/r+ option
#file.write("hello")
#file.close()