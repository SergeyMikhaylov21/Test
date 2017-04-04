import sqlite3, os

con = sqlite3.connect('demo5.db') #создание базы данных
#print(os.listdir('.'))
cur = con.cursor() #следующий этап создания базы данных
cur.execute('create table users(id integer primary key, name varchar(100))') #исполнить команду
con.commit() #закоммитить запрос
cur.execute('insert into users (id, name) values (1, "Petr")')
con.commit()
cur.execute('insert into users (id, name) values (2, "Vasya")')
con.commit()
id_var = 3
name = "Masha"
cur.execute('insert into users (id, name) values (' + str(id_var) + ', "' + name + '")')
con.commit()
cur.execute('select * from users')
print(cur.fetchall())
