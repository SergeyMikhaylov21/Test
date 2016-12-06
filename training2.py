import re
reg = '(б[аоуыиюяёэ])'
with open ('C:\\Users\\student\\Desktop\\newtext.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    words = s.split()
    for word in words:
        if re.search (reg, word):
            res = re.search (reg, word)
            print (res.group(1))
