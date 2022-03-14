new_dict={"idan":100,"ben":200,"dudu":300,"david":400,"meir":500}

print(new_dict)

summary=new_dict["idan"]+new_dict["meir"]

print("\nidan and meir total: " + str(summary))
#new dict gal = idan and meir summary's value
new_dict["gal"]=summary
print(new_dict)

print("\nNumber of entries: " + str(len(new_dict)))
print("\nidan" in new_dict)
