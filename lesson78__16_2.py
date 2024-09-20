#Домашнее задание по теме "Валидация данных".

from fastapi import FastAPI, Path
from typing import Annotated

#  создаем приложение
app = FastAPI()

# писываем маршруты
@app.get('/')
async def welcome():
    return 'Главная страница'
@app.get('/user/admin')
async def admin_page():
    return 'Вы вошли как администратор'


@app.get("/user/{username}/{age}")
async def user_name_age(
        username: Annotated[str, Path(min_length=3, max_length=20, description='Имя пользователя', example='Оля')],
        age: Annotated[int, Path(ge=12, le=120, description='Возраст', example=55)]):
    return f'Информация о пользователе. Имя: {username}, возраст: {age}'


@app.get("/user/{user_id}")
async def user_id(user_id: Annotated[int, Path(ge=1, le=1000, description='Enter User ID', example='55')]):
    return f'Вы вошли как пользователь № {user_id}'
