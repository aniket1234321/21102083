i = input("enter number :")
i = int(i)
Sum = 0

for e in range(1, i):
    if i % e == 0:
        Sum += e

if i == Sum:
    print(f"{Sum} is perfect number")
else:
    print("try another number")




