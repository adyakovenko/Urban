from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated
from pydantic import BaseModel
import uvicorn
from fastapi.openapi.models import Example

app = FastAPI()


class User(BaseModel):
    user_id: int
    username: str
    age: int

# users = [
#     User(user_id=1, username='UrbanUser', age=24),
#     User(user_id=2, username='UrbanTest', age=36),
#     User(user_id=3, username='Admin', age=42)
# ]
users = []


@app.get('/users')
async def get_all_users() -> list[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(
        username=Annotated[str, Path()],
        age=Annotated[int, Path(ge=0)]
) -> User:
    user_id = users[-1].user_id + 1 if len(users) > 0 else 1
    users.append(User(user_id=user_id, username=str(username), age=int(age)))
    return users[-1]


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id=Annotated[int, Path()],
        username=Annotated[str, Path()],
        age=Annotated[int, Path(ge=0)]
) -> User:
    for user in users:
        if user.user_id == int(user_id):
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    for i in range(len(users)):
        if users[i].user_id == int(user_id):
            return users.pop(i)
    raise HTTPException(status_code=404, detail='User was not found')
