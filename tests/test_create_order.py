import allure

import data
from stellarburgers_api import StellarBurgersApi

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и валидными ингредиентами")
    @allure.description("Проверяет успешное создание заказа авторизованным пользователем с валидными ингредиентами.")
    def  test_create_order_with_authorization_and_valid_ingredients_returns_success(self, register_new_user_and_return_credentials, make_order_body_ingredients):
        user = register_new_user_and_return_credentials
        token = user['access_token']
        headers = StellarBurgersApi.auth_headers(token)
        payload = make_order_body_ingredients

        response = StellarBurgersApi.create_order(payload, headers=headers)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа без авторизации с валидными ингредиентами")
    @allure.description("Проверяет успешное создание заказа без авторизации с валидными ингредиентами.")
    def test_create_order_without_authorization_with_valid_ingredients_returns_success(self, make_order_body_ingredients):
        payload = make_order_body_ingredients

        response = StellarBurgersApi.create_order(payload)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверяет, что создание заказа без ингредиентов возвращает ошибку 400.")
    def test_create_order_without_ingredients_returns_400_error(self):
        payload = {}

        response = StellarBurgersApi.create_order(payload)

        assert response.status_code == 400
        assert response.json()['success'] == False
        assert response.json()['message'] == data.ERROR_MESSAGE_INGREDIENTS_REQUIRED

    @allure.title("Создание заказа с невалидными ингредиентами")
    @allure.description("Проверяет, что создание заказа с невалидными ингредиентами возвращает ошибку 500.")
    def test_create_order_with_invalid_ingredients_returns_500_error(self): # проверяет создание заказа с невалидными ингредиентами
        payload = {
            "ingredients": [
                "fakeidingredient",
                "anotherfakeid"
            ]
        }

        response = StellarBurgersApi.create_order(payload)

        assert response.status_code == 500






