# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)

''')

# 1. заполняем базу
for i in range(1, 11):
    cursor.execute(' INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'user{i}', f'example{i}@mail.ru', i*10, 1000))

# 2. Обновите balance у каждой 2ой записи начиная с 1ой на 500:
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for i in range(1, len(users) + 1, 2):
    cursor.execute( 'UPDATE Users SET balance = ? WHERE id= ? ', (500, i))

# 3. Удалите каждую 3ую запись в таблице начиная с 1ой:

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for i in range (1, len(users) + 1, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

# 4. Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
cursor.execute('SELECT * FROM Users WHERE age != ?',(60,))
users = cursor.fetchall()
_ = [print(f'Имя:{x[1]} | Почта:{x[2]} | Возраст:{x[3]} | Баланс:{x[4]}') for x in users]
connection.commit()
connection.close()