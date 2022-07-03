I = [1, 1]
n = int(input("enter no. of row"))
print([1])
for _ in range(n):
    lst = []
    Sum = 0
    for e in range(0, len(I) - 1):
        Sum = I[e] + I[e + 1]
        lst.append(Sum)
    I = [1] + lst + [1]
    print(I)
