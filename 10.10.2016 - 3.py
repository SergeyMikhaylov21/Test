f = open (r'C:\Users\student\Desktop\Wiki-текст.txt', encoding='utf-8')
S = f.read ()
a = S.split ()
for word in a:
    word = word.strip ('.', ',', '?', '!')
word = word.lower ()
d = {}
if word in d:
    d[word] += 1
else:
    d[word] = 1
for word in sorted (d):
    print (word, d[word])
f.close ()

