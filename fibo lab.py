fibo=[1,2,3,5,8,13,21,34]

boolean="True"
for i in range(2, len(fibo)):
    print(fibo[i])
    print(fibo[i-1])
    print(fibo[i-2])
    print("\n")
    if fibo[i]!=(fibo[i-1]+fibo[i-2]):
        boolean="False"
        break

if boolean=="True":
    print("\nIt is fibo series")
else:
    print("It isn't fibo series")