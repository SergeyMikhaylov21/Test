word = input('Введите потенциально банановое слово')
a = list (word)
if a[-1] != 'а' or 'о' or 'у' or 'и' or 'ы' or 'э' or 'ю' or 'я':
    print ('не банановое слово')
elif a[::1] == 'а' or 'о' or 'у' or 'и' or 'ы' or 'э' or 'ю' or 'я':
    print ('банановое слово')
elif a[::1] != 'а' or 'о' or 'у' or 'и' or 'ы' or 'э' or 'ю' or 'я':
    print ('не банановое слово')

