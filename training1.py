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
