i = input("enter your string : ")
i = i.replace(' ', '')
lst = set(i)
lst = list(lst)
#print(lst)

alphabets = 'qwertyuioplkjhgfdsazxcvbnm'
alphabets = list(alphabets)
#print(alphabets)


check = 0
for i in lst:
    if i in alphabets:
        check += 1


if check == len(alphabets):
    print('yes')
else:
    print('no')
