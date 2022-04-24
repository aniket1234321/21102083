check = True
while check:
    try:
        a = (a1, a2, a3, a4, a5) = input().split()
        lst = []
        for i in a:
            lst.append(i)

    except:
        print('try again')
    else:
        print(lst)
        check = False

    lst.sort()
    print(lst)
