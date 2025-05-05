import allure

import data
from stellarburgers_api import StellarBurgersApi

@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:

    @allure.title("Получение заказов авторизованным пользователем")
    @allure.description("Проверяет, что авторизованный пользователь может получить список своих заказов.")
    def test_get_orders_with_authorization_returns_user_orders(self, register_new_user_and_return_credentials,
                                                               make_order_body_ingredients):
        user = register_new_user_and_return_credentials
        token = user['access_token']
        headers = StellarBurgersApi.auth_headers(token)
        payload = make_order_body_ingredients

        StellarBurgersApi.create_order(payload, headers)
        response = StellarBurgersApi.get_order_user(headers)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['orders'][0]['ingredients'] == payload['ingredients']

    @allure.title("Получение заказов без авторизации")
    @allure.description("Проверяет, что неавторизованный пользователь не может получить список заказов.")
    def test_get_orders_without_authorization_fails_with_401(self):  # получение заказа без авторизации
        response = StellarBurgersApi.get_order_user()

        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == data.ERROR_MESSAGE_UNAUTHORIZED
