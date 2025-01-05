from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn
from fastapi.openapi.models import Example

app = FastAPI()


@app.get('/')
async def main() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def hi() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user_id(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', Example=1)]) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get('/user/{username}/{age}')
async def user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', Example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', Example=24)]) \
        -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
