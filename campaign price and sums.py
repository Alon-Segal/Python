facebook=100
instagram=50

budget=int(input("What is your marketing budget?: "))
time1=int(input("How long do you want the Facebook campaign will run?: "))
time2=int(input("How long do you want the Instagram campaign will run?: "))
sum=(time1*facebook)+(time2*instagram)
sum1=sum*1.17
short=sum1-budget
print("\nSummary: " + str(sum1))
if budget >= sum1:
    print("\nSummary: " + str(sum) + " ILS before tax\nSummary include tax: " + str("%.2f" % (sum*1.17)))
    print("\nsuccessful")

else:
    print("\nYou need to add: " + str(short) + " ILS")