import requests
import urls
class StellarBurgersApi:

    @staticmethod
    def auth_headers(token):
        return {"Authorization": token}

    @staticmethod
    def create_user(body):
        return requests.post(urls.CREATE_USER, json=body)

    @staticmethod
    def delete_user(headers):
        return requests.delete(urls.USER_DATA_MANAGEMENT_URL, headers=headers)

    @staticmethod
    def login_user(body):
        return requests.post(urls.LOGIN_USER, json=body)

    @staticmethod
    def update_user(body, headers=None):
        if headers is None:
            headers = {}
        return requests.patch(urls.USER_DATA_MANAGEMENT_URL, json=body, headers=headers)

    @staticmethod
    def create_order(body, headers=None):
        if headers is None:
            headers = {}
        return requests.post(urls.ORDERS_ENDPOINT, json=body, headers=headers)


    @staticmethod
    def get_order_user(headers=None):
        if headers is None:
            headers = {}
        return requests.get(urls.ORDERS_ENDPOINT, headers=headers)

    @staticmethod
    def get_ingredients():
        return requests.get(urls.GET_INGREDIENTS)
