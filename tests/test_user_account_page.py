from pages.main_page import MainPage
from pages.user_account_page import UserAccountPage
from conftest import driver
import allure
import stellar_burger_api


class TestPersonalAccountPage:
    @allure.title('Проверка открытия личного кабинета авторизованного пользователя')
    @allure.description('Проверка открытия окна "Личный кабинет" по клику "Личный кабинет"')
    def test_open_personal_account_success(self, driver):
        # Создаём нового пользователя
        user_data = stellar_burger_api.create_user_body()
        user_response = stellar_burger_api.create_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        # Заходим в личный кабинет
        account_page = UserAccountPage(driver)
        account_page.set_email(email)
        account_page.set_password(password)
        account_page.click_enter_button()
        main_page.find_main_page_title()
        # Переходим в личный кабинет по кнопке "Личный кабинет"
        main_page.click_account_button()
        assert account_page.check_account_description()

    @allure.title('Проверка перехода в раздел "История заказов"')
    @allure.description('Проверка открытия окна "История заказов" "авторизованного пользователя')
    def test_redirect_to_order_history_page_success(self, driver):
        # Создаём нового пользователя
        user_data = stellar_burger_api.create_user_body()
        user_response = stellar_burger_api.create_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        # Заходим в личный кабинет
        account_page = UserAccountPage(driver)
        account_page.set_email(email)
        account_page.set_password(password)
        account_page.click_enter_button()
        main_page.find_main_page_title()
        # Переходим в личный кабинет
        main_page.click_account_button()
        account_page.click_order_history_btn()
        current_url = account_page.check_order_history_page_url()
        assert current_url is True

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверка выхода из аккаунта кликом по кнопке "Выход" в окне "Личный кабинет"')
    def test_exit_account_success(self, driver):
        # Создаём нового пользователя
        user_data = stellar_burger_api.create_user_body()
        user_response = stellar_burger_api.create_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        # Заходим в личный кабинет
        account_page = UserAccountPage(driver)
        account_page.set_email(email)
        account_page.set_password(password)
        account_page.click_enter_button()
        main_page.find_main_page_title()
        # Заходим в личный кабинет
        main_page.click_account_button()
        account_page.click_exit_btn()
        account_page.find_login_page_title()
        current_url = account_page.check_login_page_url()
        assert current_url is True
        