import math
# 1.
print('==>>answer for (3+4)*5 : ', (3+4)*5)

# 2
print("==>>for n(n-1)/2 : ")
n = int(input('enter value of n : '))
print(n*(n-1)/2)
# 3
pi = math.pi
print('==>>formula for surface area 4(pi)r**2')
radius = int(input('enter radius of curve :'))
print(4*pi*(radius**2))
# 4
#radius=int(input('radius : '))
# r=radius
# print(r)


# 4
print('==>>enter values of y1,y2,x1,x2')
y2 = int(input('enter y2: '))
y1 = int(input('enter y1: '))
x1 = int(input('enter x1: '))
x2 = int(input('enter x2: '))
if(x1 == x2):
    print("not defined")
else:
    print('value for (y1-y2)/(x1-x2) :', (y1-y2)/(x1-x2))
