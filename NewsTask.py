import os
news = os.listdir ('C:\\Users\\student\\Desktop\\Yandex.News')
textfile = []
for file in news:
    with open ('C:\\Users\\student\\Desktop\\Yandex.News\\' + file, encoding='utf-8') as f:
        textfile.write(file)






















