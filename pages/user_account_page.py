from pages.base_page import BasePage
import locators
import allure
import urls


class UserAccountPage(BasePage):
    @allure.step('Ввод email')
    def set_email(self, email):
        input_email = self.wait_and_find_element(locators.UserAccountLocators.FIELD_EMAIL)
        input_email.send_keys(email)

    @allure.step('Ввод пароля')
    def set_password(self, password):
        input_password = self.wait_and_find_element(locators.UserAccountLocators.FIELD_PASSWORD)
        input_password.send_keys(password)

    @allure.step('Клик по кнопке "Войти"')
    def click_enter_button(self):
        enter_button = self.wait_and_find_element(locators.UserAccountLocators.ENTER_BUTTON)
        self.click_element(enter_button)

    @allure.step('Клик по кнопке "История заказов" в личном кабинете')
    def click_order_history_btn(self):
        order_history_btn = self.wait_and_find_element(locators.UserAccountLocators.ORDER_HISTORY_BTN)
        self.click_element(order_history_btn)

    @allure.step('Клик по кнопке "Выход" в личном кабинете')
    def click_exit_btn(self):
        exit_btn = self.wait_and_find_element(locators.UserAccountLocators.EXIT_BTN)
        self.click_element(exit_btn)

    @allure.step('Получение номера последнего заказа')
    def get_order_number(self):
        element = self.wait_and_find_element(locators.UserAccountLocators.ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_recovery_button(self):
        recovery_button = self.wait_and_find_element(locators.UserAccountLocators.RECOVERY_BUTTON)
        self.click_element(recovery_button)

    @allure.step('Проверка открытия личного кабинета')
    def check_account_description(self):
        if self.is_element_present(locators.UserAccountLocators.DESCRIPTION_ACCOUNT):
            return True

    @allure.step('Проверка открытия экрана авторизации')
    def find_login_page_title(self):
        if self.is_element_present(locators.UserAccountLocators.TITLE_LOGIN_PAGE):
            return True

    @allure.step('Сравнение URL текущей страницы с адресом страницы "История заказов"')
    def check_order_history_page_url(self):
        return self.driver.current_url == urls.ORDER_HISTORY_URL

    @allure.step('Сравнение URL текущей страницы с адресом страницы входа в аккаунт')
    def check_login_page_url(self):
        return self.driver.current_url == urls.LOGIN_URL
