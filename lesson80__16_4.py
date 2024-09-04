# Домашнее задание по теме "Модели данных Pydantic"

from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

#  создаем приложение
app = FastAPI()

# создаем 'БД'
db_users = []

# создаем класс User потомок BaseModel

class User(BaseModel):
    id: int = None
    username: str
    age: int

# описываем 4 CRUD запроса

@app.get('/users') # показывает всю БД пользователей
async def get_all_users() -> list[User]:
    return db_users

@app.post('/user/{username}/{age}') # добавляет запись в БД пользователей
async def add_user(username: Annotated[str, Path(min_length=2,max_length=20, description='Введите имя пользователя',
                                                 example='Ян или Example_2: LePage73')],
                   age: Annotated[int, Path(gt=12 , lt= 130, description='Введите возраст', example=55)])-> User:
    if len(db_users) == 0:
        user_id = 1
    else:
        user_id = db_users[-1].id + 1  # по заданию "id этого объекта будет на 1 больше, чем у последнего в списке users"
    db_users.append(User(id = user_id, username = username, age = age)) # добавляем новую запись с новым индексом
    return User(id = user_id, username = username, age = age)

@app.put('/user/{user_id}/{username}/{age}') # обновляет по ID запись пользователя в БД
async def update_user(user_id: Annotated[int, Path(gt=0, lt=1000, description='Введите ID пользователя', example=123)],
                      username: Annotated[str, Path(min_length=2,max_length=20, description='Введите имя пользователя',
                                                 example='Ян или Example_2: LePage73')],
                      age: Annotated[int, Path(gt=12 , lt= 130, description='Введите возраст', example=55)]) -> User:

    user_idx = [i for i,x in enumerate(db_users) if user_id == x.id] # находми индекс запись с нужным ID
    try:
        edit_user = db_users[user_idx[0]] # выбираем нужного пользователя
        edit_user.username = username # меняем имя
        edit_user.age = age # меняем возраст
    except IndexError:
        raise HTTPException(status_code=404, detail=f'User ID {user_id} was not found')
    return edit_user

@app.delete('/user/{user_id}') # удаляет запись с ключом ID
async def delete_user(user_id: Annotated[int, Path(gt=0, lt=1000, description='Введите ID пользователя', example=123)]) -> User:
    user_idx = [i for i, x in enumerate(db_users) if user_id == x.id]  # находми индекс запись с нужным ID
    try:
        return db_users.pop(user_idx[0])
    except IndexError:
        raise HTTPException(status_code=404, detail=f'User ID {user_id} was not found')


