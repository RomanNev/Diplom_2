import allure
import requests
import urls
class StellarBurgersApi:

    @staticmethod
    def auth_headers(token):
        return {"Authorization": token}

    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(body):
        return requests.post(urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(headers):
        return requests.delete(urls.USER_DATA_MANAGEMENT_URL, headers=headers)

    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(body):
        return requests.post(urls.LOGIN_USER, json=body)

    @staticmethod
    @allure.step("Обновление данных пользователя")
    def update_user(body, headers=None):
        if headers is None:
            headers = {}
        return requests.patch(urls.USER_DATA_MANAGEMENT_URL, json=body, headers=headers)

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(body, headers=None):
        if headers is None:
            headers = {}
        return requests.post(urls.ORDERS_ENDPOINT, json=body, headers=headers)


    @staticmethod
    @allure.step("Получение заказов пользователя")
    def get_order_user(headers=None):
        if headers is None:
            headers = {}
        return requests.get(urls.ORDERS_ENDPOINT, headers=headers)

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients():
        return requests.get(urls.GET_INGREDIENTS)
