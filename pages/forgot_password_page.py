from pages.base_page import BasePage
import locators
import allure


class RecoveryPasswordPage(BasePage):
    @allure.step('Ввод email')
    def set_email(self, email):
        input_email = self.wait_and_find_element(locators.ForgotPassPageLocators.FIELD_EMAIL)
        input_email.send_keys(email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_button_recovery(self):
        recovery_button = self.wait_and_find_element(locators.ForgotPassPageLocators.BUTTON_RECOVERY)
        self.click_element(recovery_button)

    @allure.step('Ввод нового пароля')
    def set_new_password(self, password):
        input_password = self.wait_and_find_element(locators.ForgotPassPageLocators.FIELD_NEW_PASSWORD)
        input_password.send_keys(password)

    @allure.step('Клик по кнопке отображения скрытого пароля')
    def click_show_password_button(self):
        eye_button = self.wait_and_find_element(locators.ForgotPassPageLocators.EYE_BUTTON)
        self.click_element(eye_button)

    @allure.step('Состояние поля пароля')
    def get_password_input_state(self):
        input_password = self.wait_and_find_element(locators.ForgotPassPageLocators.FIELD_NEW_PASSWORD)
        return input_password.get_attribute("type") == "text"

    @allure.step("Проверка открытия экрана восстановления пароля")
    def check_recovery_page_title(self):
        if self.is_element_present(locators.ForgotPassPageLocators.RECOVER_TITLE):
            return True

