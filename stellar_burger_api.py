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

@allure.step("Получение access token пользователя")
def get_access_token(user_response):
    access_token = user_response.json().get("accessToken")
    return access_token

@allure.step("Удаление пользователя")
def delete_user(access_token):
    headers = {"Authorization": access_token}
    response_delete = requests.delete(urls.DELETE_USER_URL, headers=headers)
    return response_delete
