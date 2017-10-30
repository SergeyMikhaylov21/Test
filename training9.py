<<<<<<< HEAD
﻿<<<<<<< HEAD

s = input ('Введите слово')

a = list (s)

for indx, digit in enumerate (a):
    
	if indx % 2 != 0:
        
a[indx] = 'ы'

s1 = ''.join (a)

print (s1)



=======

s = input ('Введите слово')
a = list (s)
for indx, digit in enumerate (a):
    if indx % 2 != 0:
        a[indx] = 'ы'
s1 = ''.join (a)
print (s1)

>>>>>>> 4f347025a65bfb532012492ec3fd059dfad61746
=======
import re
reg = '[а-яёА-ЯЁ]'
with open ('C:\\Users\\student\\Desktop\\newtext.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    words = s.split()
    count = len(words)
    i = 0
    for word in words:
        if re.search (reg, word):
            i += 1
    if count != i:
        print (i, count)
    else:
        print (count)
>>>>>>> d3271ff4db93b53068c0833d15cd951c7ac22e31
