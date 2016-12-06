import re
reg = '[аоуыиюяёэ]'
with open ('C:\\Users\\student\\Desktop\\newtext.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    words = s.split()
    a = re.findall(reg, s)
    print (len(a))
