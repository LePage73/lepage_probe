from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
    pass

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int
    pass

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
    pass

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
    pass