import string
import random


def new_user_login_password():
    def generate_random_string(length):
        new_name = ''.join(random.choices(string.ascii_lowercase, k=7))
        new_email = ''.join(random.choices(string.ascii_lowercase, k=7)) + '@yandex.ru'
        new_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=6))
        registration_data = {
            "email": new_email,
            "password": new_password,
            "name": new_name
        }
        return registration_data
