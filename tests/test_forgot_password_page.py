from pages.main_page import MainPage
from pages.forgot_password_page import RecoveryPasswordPage
from pages.user_account_page import UserAccountPage
from conftest import driver
import data
import allure


class TestRecoveryPassPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('Проверяем клик по кнопке "Восстановить пароль"')
    def test_success_recovery_pass(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        # Переход в окно личный кабинет
        main_page.click_account_button()
        account_page = UserAccountPage(driver)
        account_page.click_recovery_button()
        # переход в окно восстановление пароля
        recovery_page = RecoveryPasswordPage(driver)
        assert recovery_page.check_recovery_page_title()

    @allure.title('Проверка восстановления пароля после ввода email')
    @allure.description('Проверяем ввод почты и клик по кнопке "Восстановить"')
    def test_input_email_and_click_button_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        # Переход в окно личный кабинет
        main_page.click_account_button()
        account_page = UserAccountPage(driver)
        account_page.click_recovery_button()
        # Переход в окно восстановление пароля
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(data.my_email)
        recovery_page.click_button_recovery()
        assert recovery_page.check_recovery_page_title()

    @allure.title('Проверка работы кнопки скрытия пароля')
    @allure.description('Проверяем отображение пароля после клика по кнопке скрытия пароля ')
    def test_eye_button_show_password_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        # Переход в окно личный кабинет
        account_page = UserAccountPage(driver)
        account_page.click_recovery_button()
        # Переход в окно восстановление пароля
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(data.my_email)
        recovery_page.click_button_recovery()
        recovery_page.set_new_password(data.my_new_password)
         # Проверяем ввод старого и нового пароля
        old_state = recovery_page.get_password_input_state()
        recovery_page.click_show_password_button()
        new_state = recovery_page.get_password_input_state()
        assert old_state is False and new_state is True
