# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."

from fastapi import FastAPI, Path
from typing import Annotated

#  создаем приложение
app = FastAPI()

# создаем 'БД'
db_users = {'1': 'Имя: Example, возраст: 18'}

# описываем 4 CRUD запроса

@app.get('/users') # показывает всю БД пользователей
async def get_all_users() -> dict:
    return db_users
@app.post('/user/{username}/{age}') # добавляет запись в БД пользователей
async def add_user(username: Annotated[str, Path(min_length=2,max_length=20, description='Введите имя пользователя',
                                                 example='Ян или Example_2: LePage73')],
                   age: Annotated[int, Path(gt=12 , lt= 130, description='Введите возраст', example=55)])-> str:
    next_db_index = str(int(max(db_users, key=int)) + 1) # вычисляем следующий индекс в БД
    db_users[next_db_index] = f'Имя: {username}, возраст: {age}' # добавляем запись с новым индексом
    return f'User with ID: {next_db_index} - \'Имя: {username}, возраст: {age}\' is registered'
@app.put('/user/{user_id}/{username}/{age}') # обновляет по ID запись пользователя в БД
async def update_user(user_id: Annotated[int, Path(gt=0, lt=1000, description='Введите ID пользователя', example=123)],
                      username: Annotated[str, Path(min_length=2,max_length=20, description='Введите имя пользователя',
                                                 example='Ян или Example_2: LePage73')],
                      age: Annotated[int, Path(gt=12 , lt= 130, description='Введите возраст', example=55)]) -> str:
    db_users[user_id] = f'Имя: {username}, возраст: {age}' # меняем в записи с указанным ID значения
    return f'The User with ID: {user_id} - \'Имя: {username}, возраст: {age}\' is Re-registered'
@app.delete('/user/{user_id}') # удаляет запись с ключом ID
async def delete_user(user_id: Annotated[int, Path(gt=0, lt=1000, description='Введите ID пользователя', example=123)]) -> str:
    return f'User ID {user_id}, - {db_users.pop(user_id)}, has been deleted'

