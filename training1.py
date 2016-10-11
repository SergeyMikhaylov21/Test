s = input ('Введите слово')
a = list (s)
for indx, digit in enumerate (a):
    if indx % 2 != 0:
        a[indx] = 'ы'
s1 = ''.join (a)
print (s1)

