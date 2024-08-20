# Домашнее задание по теме "План написания админ панели"

import sqlite3

connection = sqlite3.connect('product_telegramm.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
picture_file_name TEXT,
price INTEGER NOT NULL
)

''')
# 1. Чистим базу если остались значения от предыдущих запусков
cursor.execute('DELETE FROM Products ')
connection.commit()

# 2. Заполняем заново
for i in range(1, 5):
    cursor.execute(f'''
    INSERT INTO Products VALUES('{i}','Продукт{i}', 'Описание{i}', '.\\Picture{i}.jpg', '{i*100}')
    ''')
connection.commit()
connection.close()

# 3. Вырбать все продукты
def get_all_products():
    connection = sqlite3.connect('product_telegramm.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products
# 4. дополните созданием таблицы Users
def initiate_db():
    connection = sqlite3.connect('product_telegramm.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INTEGER NOT NULL
    )

    ''')
    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection = sqlite3.connect('product_telegramm.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)',(username, email, age))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('product_telegramm.db')
    cursor = connection.cursor()
    is_ = cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?',(username,)).fetchone()[0]
    if is_ == 0: return False
    else: return True


initiate_db()