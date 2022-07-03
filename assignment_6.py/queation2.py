n = input('enter string : ')
n = n.replace(' ', '')
if n == n[::-1]:
    print("palindrome")
else:
    print('try again')