from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from pages.base_page import BasePage
import urls
import locators
import allure


class MainPage(BasePage):
    @allure.step('Открываем в браузере главную страницу "Stellar Burger"')
    def open(self):
        self.open_page(urls.BASE_PAGE)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_list_order_button(self):
        list_order_button = self.wait_and_find_element(locators.MainPageLocators.LIST_ORDER_BTN)
        self.click_element(list_order_button)

    @allure.step('Клик по ингредиенту')
    def click_ingredient_button(self):
        ingredients_list = self.wait_and_find_element(locators.MainPageLocators.INGREDIENT_LIST)
        ingredients = ingredients_list.find_elements(*locators.MainPageLocators.INGREDIENT_ITEM)
        second_ingredient = ingredients[1]
        self.click_element(second_ingredient)

    @allure.step('Клик по кнопке закрытия всплывающего окна')
    def close_ingredient_card(self):
        x_button = self.wait_and_find_element(locators.MainPageLocators.X_BUTTON)
        self.click_element(x_button)

    @allure.step('Drag ans drop булку в зону создания бургера')
    def add_bun_in_order(self):
        source = self.wait_and_find_element(locators.MainPageLocators.BUN_INGREDIENT)
        target = self.wait_and_find_element(locators.MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step('Drag ans drop соус в зону создания бургера')
    def add_sauce_in_order(self):
        source = self.wait_and_find_element(locators.MainPageLocators.SAUCE_INGREDIENT)
        target = self.wait_and_find_element(locators.MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step('Drag ans drop начинку в зону создания бургера')
    def add_meat_in_order(self):
        source = self.wait_and_find_element(locators.MainPageLocators.MEAT_INGREDIENT)
        target = self.wait_and_find_element(locators.MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_create_order_button(self):
        account_button = self.wait_and_find_element(locators.MainPageLocators.CREATE_ORDER_BTN)
        self.click_element(account_button)

    @allure.step('Получаем количество ингредиентов')
    def get_count_ingredient(self):
        counter_element = self.wait_and_find_element(locators.MainPageLocators.COUNTER)
        return counter_element.text

    @allure.step('Получаем Email для авторизации из сгенерированных данных')
    def get_user_email(self, user_response):
        email = user_response["email"]
        return email

    @allure.step('Получаем пароль для авторизации из сгенерированных данных')
    def get_user_password(self, user_response):
        password = user_response["password"]
        return password

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_account_button(self):
        account_button = self.wait_and_find_element(locators.MainPageLocators.BUTTON_ACCOUNT)
        self.click_element(account_button)

    @allure.step('Клик по кнопке закрытия всплывающего окна')
    def click_order_card_x_button(self):
        x_button = self.wait_and_find_element(locators.MainPageLocators.CLOSE_WINDOW_BTN)
        self.click_element(x_button)

    @allure.step('Получение номер оформленного заказа')
    def get_new_order_number(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.wait_and_find_element(locators.MainPageLocators.NUMBER_NEW_ORDER).text != '9999')
        new_order_number_element = self.wait_and_find_element(locators.MainPageLocators.NUMBER_NEW_ORDER)
        new_order_number = new_order_number_element.text
        return int(new_order_number)

    @allure.step('Проверка названия ингредиента')
    def check_ingredient_title(self):
        if self.is_element_present(locators.MainPageLocators.INGREDIENT_TITLE):
            return True

    @allure.step('Проверка закрытия карточки ингредиаента')
    def check_main_page_title(self):
        if self.is_element_present(locators.MainPageLocators.TITLE_MAIN_PAGE):
            return True

    @allure.step('Открытие главной страницы')
    def find_main_page_title(self):
        return self.wait_and_find_element(locators.MainPageLocators.TITLE_MAIN_PAGE)

    @allure.step('Открытие страницы ленты заказа')
    def find_create_order_description(self):
        return self.wait_and_find_element(locators.MainPageLocators.CREATE_ORDER_DESCRIPTION)

    @allure.step('Сравнение URL текущей страницы с адресом страницы "Лента заказов"')
    def check_order_list_url(self):
        return self.driver.current_url == urls.LIST_ORDER_PAGE
