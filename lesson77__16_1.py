from fastapi import FastAPI

#  создаем приложение
app = FastAPI()


# писываем маршруты
@app.get('/')
async def welcome():
    return 'Главная страница'

@app.get('/user/admin')
async def admin_page():
    return 'Вы вошли как администратор'
@app.get("/user")
async def user_name_age(user: str, age: int):
    return f'Информация о пользователе. Имя: {user}, возраст: {age}'
@app.get("/user/{user_id}")
async def user_id(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'

