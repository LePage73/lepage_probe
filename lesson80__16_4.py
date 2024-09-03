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
    db_users.append(User(id = len(db_users), username = username, age = age)) # добавляем запись с новым индексом
    return User(id = len(db_users), username = username, age = age)
@app.put('/user/{user_id}/{username}/{age}') # обновляет по ID запись пользователя в БД
async def update_user(user_id: Annotated[int, Path(gt=0, lt=1000, description='Введите ID пользователя', example=123)],
                      username: Annotated[str, Path(min_length=2,max_length=20, description='Введите имя пользователя',
                                                 example='Ян или Example_2: LePage73')],
                      age: Annotated[int, Path(gt=12 , lt= 130, description='Введите возраст', example=55)]) -> User:
    try:
        edit_user = db_users[user_id] # ищем пользователя с таким ID
        edit_user.username = username # меняем имя
        edit_user.age = age # меняем возраст
    except IndexError:
        raise HTTPException(status_code=404, detail=f'User ID {user_id} was not found')
    return edit_user
@app.delete('/user/{user_id}') # удаляет запись с ключом ID
async def delete_user(user_id: Annotated[int, Path(gt=0, lt=1000, description='Введите ID пользователя', example=123)]) -> User:
    try:
        return db_users.pop(user_id)
    except IndexError:
        raise HTTPException(status_code=404, detail=f'User ID {user_id} was not found')


