from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/user/admin')
async def welcom_a():
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async  def welcom_i(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='50')]):
    return {'message': f'Вы вошли как пользователь № {user_id}'}



@app.get('/user/{username}/{age}')
async def welcom_u(username: Annotated[str, Path(min_length=5, max_length=20,
                                                 description='Enter username',
                                                 example='UrbanUser')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get('/')
async def welcom():
    return {'message': 'Главная страница'}