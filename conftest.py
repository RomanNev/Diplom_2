import pytest

from helper import Helper
from stellarburgers_api import StellarBurgersApi

@pytest.fixture # создание кредов для пользователя и удаления пользователя по этим данным
def manage_user_credentials():
    payload = Helper.generate_credentials_user()
    yield payload # вернули пользователя креды в тест
    # удаление пользователя
    response = StellarBurgersApi.login_user(payload) # логинимся под пользователем из теста
    if response.status_code == 200:
        access_token = response.json()["accessToken"] # тащим токен
        headers = StellarBurgersApi.auth_headers(access_token)
        test = StellarBurgersApi.delete_user(headers=headers) # удаляем передав токен

@pytest.fixture()
def register_new_user_and_return_credentials(): # регистрация и удаление пользователя
    payload = Helper.generate_credentials_user()
    response = StellarBurgersApi.create_user(payload)
    if response.status_code == 200:
        access_token = response.json()["accessToken"]
        yield {
            "payload": payload,
            "access_token": access_token
        } # возвращаем в тест креды и токен
        headers = StellarBurgersApi.auth_headers(access_token)
        test = StellarBurgersApi.delete_user(headers=headers)  # удаляем передав токен
    else:
        pytest.fail(f"Не удалось зарегистрировать пользователя: {response.status_code}, {response.text}")

@pytest.fixture()
def get_ingredients(): # получаем список ингредиентов
    response = StellarBurgersApi.get_ingredients()
    ingredients = response.json()["data"]
    return ingredients

@pytest.fixture()
def make_order_body_ingredients(get_ingredients):
    return {
            "ingredients": [get_ingredients[0]['_id']], # берем первый id и передаем в тест
        }







