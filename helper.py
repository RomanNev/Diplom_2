from faker import Faker
import time

fake = Faker()

class Helper:

    @staticmethod
    def generate_unique_email(): # генерируем точно уникальный email
        timestamp = int(time.time() * 1000)
        return f"{fake.first_name().lower()}.{timestamp}@example.com"

    @staticmethod
    def generate_credentials_user():
        return {
            "email": Helper.generate_unique_email(),
            "password": fake.password(),
            "name": fake.first_name()
        }
