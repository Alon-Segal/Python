
Tomatoprice=3
Cucumberprice=2
Colaprice=5
Tofuprice=10

print("\nMenu:\n\nTomato = " + str(Tomatoprice) + "\nCucumber = " + str(Cucumberprice) + "\nCoca-Cola = " + str(Colaprice) + "\nTofu = " + str(Tofuprice))

Tomato=int(input("\nHow many kg of Tomatos?: "))
Cucumber=int(input("\nHow many kg of Cucumbers?: "))
Cola=int(input("\nHow many bottles of Cola?: "))
Tofu=int(input("\nHow many kg of Tofu?: "))

print("\n\nSummary of your order:\n\nTomato: " + str(Tomato) + " kg\nCucumber: " + str(Cucumber) + " kg\nCoca-Cola: " + str(Cola) + " kg\nTofu: " + str(Tofu) + " kg")

sum=(Tomato*Tomatoprice)+(Cucumber*Cucumberprice)+(Cola*Colaprice)+(Tofu*Tofuprice)

print("\n-------\nBefore tax: " + str(sum) + "\nTotal include tax: " + str("%.2f" % (sum*1.17)))