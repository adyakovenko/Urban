from typing import Annotated

from fastapi import FastAPI, Path
import uvicorn
from fastapi.openapi.models import Example

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(
        username=Annotated[str, Path()],
        age=Annotated[int, Path(ge=0)]
) -> str:
    user_id = str(int(max(users, key=int)) + int(1))
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id=Annotated[str, Path()],
        username=Annotated[str, Path()],
        age=Annotated[int, Path(ge=0)]
) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(str(user_id))
    return f'user {user_id} has been deleted'
