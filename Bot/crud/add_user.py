# остальные импорты
import json

# импорты aiogram
from aiohttp import ClientSession

async def add_user(user_tg_id, full_name, username):
    ''' Функция делает запрос в БД на добавление пользователя'''

    data = {'user_tg_id': user_tg_id,
            'full_name': full_name,
            'username': username}
    json_data = json.dumps(data)
    async with ClientSession() as session:
        async with session.post('http://127.0.0.1:8080/user_add/', data=json_data) as response:

            response = await response.json()
            print(response)