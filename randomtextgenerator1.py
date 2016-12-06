import re
import random
reg = '[а-яёА-ЯЁ]'
def nounfunction ():
    with open ('C:\\Users\\student\\Desktop\\textnouns.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        words = s.split()
        d = []
        for word in words:
            if re.search (reg, word):
                d.append(word)
            else:
                continue
        return (random.choice(d))
def verbfunction ():
    with open ('C:\\Users\\student\\Desktop\\textverbs.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        words = s.split()
        d = []
        for word in words:
            if re.search (reg, word):
                d.append(word)
            else:
                continue
        return (random.choice(d))
def adjfunction ():
    with open ('C:\\Users\\student\\Desktop\\textadjectives.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        words = s.split()
        d = []
        for word in words:
            if re.search (reg, word):
                d.append(word)
            else:
                continue
        return (random.choice(d))
def objectfunction ():
    with open ('C:\\Users\\student\\Desktop\\text1.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        words = s.split()
        d = []
        for word in words:
            if re.search (reg, word):
                d.append(word)
            else:
                continue
        return (random.choice(d))
