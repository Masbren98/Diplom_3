import allure
import helper
import urls
import requests


@allure.step("Создание данных для создания юзера: email, password, name")
def create_user_body():
    return helper.new_user_login_password()


@allure.step("Создание нового пользователя")
def create_user(user_data):
    user_response = requests.post(urls.CREATE_USER_URL, json=user_data)
    return user_response

