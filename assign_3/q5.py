weight = {
    'h': 1.00794, 'c': 12.0107, 'o': 15.9994
}
h = int(input('no. of h atoms :'))
c = int(input('no. of c atoms :'))
o = int(input('no. of o atoms :'))

print("weight of molecules :", (weight["h"]*h+weight['c']*c+weight['o']*o))
