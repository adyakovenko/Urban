from fastapi import FastAPI, Request, Path, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated, List
import uvicorn
from fastapi.openapi.models import Example

#app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

app = FastAPI()

templates = Jinja2Templates(directory="module_16_5\\templates")


class User(BaseModel):
    user_id: int = None
    username: str
    age: int


users = [
    User(user_id=1, username='UrbanUser', age=24),
    User(user_id=2, username='UrbanTest', age=36),
    User(user_id=3, username='Admin', age=42)
]
#users = []


@app.get('/')
async def main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    for user in users:
        if user.user_id == int(user_id):
            return templates.TemplateResponse('users.html', {'request': request, 'user': user})


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
