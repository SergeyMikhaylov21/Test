<<<<<<< HEAD
a = ""
while a != 'exit':
    a = input('Введите словоформу глагола делать')
    if a == 'делает':
        b = input ('Введите род: м или ж')
        if b == 'м':
            print ('третье лицо, мужской род, единственное число')
        elif b == 'ж':
            print ('третье лицо, женский род, единственное число')
    elif a == 'делают':
        print ('третье лицо, множественное число')
    elif a == 'делаем':
        print ('первое лицо, множественное число')
    elif a == 'делаешь':
        print ('второе лицо, единственное число')
    elif a == 'делаем':
        print ('первое лицо, множественное число')
    elif a == 'делаете':
        print ('второе лицо, множественное число')
    elif a.endswith('ю'):
        print ('первое лицо, единственное число')
if a == 'exit':
    print ('Ой, все')
=======
a = ""
while a != 'exit':
    a = input('Введите словоформу глагола делать')
    if a == 'делает':
        b = input ('Введите род: м или ж')
        if b == 'м':
            print ('третье лицо, мужской род, единственное число')
        elif b == 'ж':
            print ('третье лицо, женский род, единственное число')
    elif a == 'делают':
        print ('третье лицо, множественное число')
    elif a == 'делаем':
        print ('первое лицо, множественное число')
    elif a == 'делаешь':
        print ('второе лицо, единственное число')
    elif a == 'делаем':
        print ('первое лицо, множественное число')
    elif a == 'делаете':
        print ('второе лицо, множественное число')
    elif a.endswith('ю'):
        print ('первое лицо, единственное число')
if a == 'exit':
    print ('Ой, все')
>>>>>>> 4f347025a65bfb532012492ec3fd059dfad61746