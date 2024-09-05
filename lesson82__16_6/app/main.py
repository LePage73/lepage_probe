from fastapi import FastAPI
from routers import task, user
app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Добро пожаловать в Менеджер задач'}

app.include_router(task.router)
app.include_router((user.user_router))