import re
patt = re.compile('^«[А-ЯЁ]?, [а-яё]*, [1-9]»$')
with open ('C:\\Users\\student\\Desktop\\Китай.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    words = s.split()
    for word in words:
        if patt.search(word):
            print (word)
