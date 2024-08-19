# Домашнее задание по теме "План написания админ панели"

import sqlite3

connection = sqlite3.connect('product_telegramm.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
picture_file_name TEXT,
price INTEGER NOT NULL
)

''')
# 1. Чистим базу если остались значения от предыдущих запусков
cursor.execute('DELETE FROM Users ')
connection.commit()

# 2. Заполняем заново
for i in range(1, 5):
    cursor.execute(f'''
    INSERT INTO Users VALUES('{i}','Продукт{i}', 'Описание{i}', '.\\Picture{i}.jpg', '{i*100}')
    ''')
connection.commit()
connection.close()

# 3. Вырбать все продукты
def get_all_products():
    connection = sqlite3.connect('product_telegramm.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products


