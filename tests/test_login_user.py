import allure
import pytest
from stellarburgers_api import StellarBurgersApi


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Успешный логин существующего пользователя")
    @allure.description("Проверяет, что можно авторизоваться под существующим пользователем с корректными данными.")
    def test_login_exist_user_success_response(self,
                                               register_new_user_and_return_credentials):
        user = register_new_user_and_return_credentials
        payload = user['payload']
        response = StellarBurgersApi.login_user(payload)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user']['email'] == payload['email']
        assert response.json()['user']['name'] == payload['name']
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()

    @allure.title("Логин с некорректным логином или паролем")
    @allure.description("Проверяет, что нельзя авторизоваться с неправильным логином или паролем.")
    @pytest.mark.parametrize('field, data_field', [('email', 'this_is_fake@mail.com'),
                                                   ('password', 'fake_password')
                                                   ])  # ломаем креды через параметризацию
    def test_login_with_incorrect_login_or_password(self, register_new_user_and_return_credentials, field,
                                                    data_field):
        user = register_new_user_and_return_credentials
        payload = user['payload']
        payload[field] = data_field  # сломали логин или пароль
        response = StellarBurgersApi.login_user(payload)

        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == "email or password are incorrect"
