import allure
import pytest
import data
from stellarburgers_api import StellarBurgersApi


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание нового пользователя")
    @allure.description("Проверяет успешное создание уникального пользователя с корректными данными.")
    def test_create_user_returns_200_success_response(self,
                                                      manage_user_credentials):
        payload = manage_user_credentials
        response = StellarBurgersApi.create_user(payload)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user']['email'] == payload['email']
        assert response.json()['user']['name'] == payload['name']
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()

    @allure.title("Создание уже зарегистрированного пользователя")
    @allure.description("Проверяет, что нельзя создать пользователя с уже существующими данными.")
    def test_create_user_fails_for_duplicate_create(self,
                                                    manage_user_credentials):
        payload = manage_user_credentials
        StellarBurgersApi.create_user(payload)
        response = StellarBurgersApi.create_user(payload)

        assert response.status_code == 403
        assert response.json()['success'] == False
        assert response.json()['message'] == "User already exists"

    @allure.title("Создание пользователя без обязательных полей")
    @allure.description("Проверяет, что нельзя создать пользователя, если отсутствует одно из обязательных полей.")
    @pytest.mark.parametrize('data_test',
                             [data.USER_CREDENTIALS_WITHOUT_EMAIL, data.USER_CREDENTIALS_WITHOUT_PASSWORD,
                              data.USER_CREDENTIALS_WITHOUT_NAME])
    def test_create_user_without_required_fields(self,
                                                 data_test):
        payload = data_test
        response = StellarBurgersApi.create_user(payload)

        assert response.status_code == 403
        assert response.json()['success'] == False
        assert response.json()['message'] == "Email, password and name are required fields"
