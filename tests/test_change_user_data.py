import allure
import pytest
from stellarburgers_api import StellarBurgersApi


@allure.feature("Изменение данных пользователя")
class TestChangeUserData:

    @allure.title("Обновление email или имени с авторизацией")
    @allure.description("Проверяет, что авторизованный пользователь может обновить email или имя.")
    @pytest.mark.parametrize('field, data_field', [('email', 'update_email_user@example123.com'),
                                                   ('name', 'update_name_user')
                                                   ])  # данные для обновления пользователя с параметризацией
    def test_update_email_or_name_with_authorization(self, register_new_user_and_return_credentials, field,
                                                     data_field):
        user = register_new_user_and_return_credentials
        token = user['access_token']
        payload = user['payload']
        payload[field] = data_field  # обновляем одно из полей новыми данными
        headers = StellarBurgersApi.auth_headers(token)

        response = StellarBurgersApi.update_user(payload, headers)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user'][field] == data_field

    @allure.title("Обновление пароля с авторизацией")
    @allure.description(
        "Проверяет, что авторизованный пользователь может обновить пароль и авторизоваться с новым паролем.")
    def test_update_password_with_authorization(self,
                                                register_new_user_and_return_credentials):
        user = register_new_user_and_return_credentials
        token = user['access_token']
        payload = user['payload']
        payload['password'] = "update_password_user"
        headers = StellarBurgersApi.auth_headers(token)

        StellarBurgersApi.update_user(payload, headers)  # обновляем пароль
        response = StellarBurgersApi.login_user(payload)  # проверяем, что можно залогиниться с новым паролем

        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title("Обновление данных без авторизации")
    @allure.description("Проверяет, что нельзя изменить данные пользователя без авторизации.")
    @pytest.mark.parametrize('field, data_field', [('email', 'update_email_user@example123.com'),
                                                   ('password', 'update_password_user'),
                                                   ('name', 'update_name_user')
                                                   ])
    def test_update_data_user_without_authorization(self, register_new_user_and_return_credentials, field,
                                                    data_field):
        user = register_new_user_and_return_credentials
        payload = user['payload']
        payload[field] = data_field  # обновляем одно из полей новыми данными

        response = StellarBurgersApi.update_user(payload)

        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == 'You should be authorised'
