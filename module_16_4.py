from fastapi import FastAPI, Path, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
# users = {'1': "Имя:Example,возраст:18"}
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_user() -> list[User]:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: str, age: int) -> User:
    if users:
        user_id = users[-1].id +1
    else:
        user_id = 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int, user: str = Body()) -> User:
   
        for user in users:
            if user.id == users_id:
                user.username = username
                user.age = age
                return user
            else:
                raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f'{user_id} DELETE'

    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")


