from pages.base_page import BasePage
import locators
import allure
import urls


class OrderListPage(BasePage):

    @allure.step("Открыть окно с деталями заказа кликом по карточке заказа")
    def click_order_card(self):
        order_card = self.wait_and_find_element(locators.OrderListPageLocators.ORDER_CARD)
        self.click_element(order_card)


    @allure.step('Получение номера последнего заказа')
    def get_order_number(self):
        element = self.wait_and_find_element(locators.OrderListPageLocators.ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step('Значение счётчика заказов на странице "Лента заказов"')
    def get_orders_counter(self):
        number = self.wait_and_find_element(locators.OrderListPageLocators.ORDER_COUNTER)
        return int(number.text)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        constructor_button = self.wait_and_find_element(locators.OrderListPageLocators.CONSTRUCTOR_BTN)
        self.click_element(constructor_button)

    @allure.step('Значение счётчика "Выполнено за сегодня" заказов на странице "Лента заказов"')
    def get_orders_counter_today(self):
        number = self.wait_and_find_element(locators.OrderListPageLocators.ORDER_COUNTER_TODAY)
        return int(number.text)

    @allure.step('Номер заказа в разделе "В работе" на экране "Ллента заказов"')
    def get_order_in_works_number(self):
        number_in_works = self.wait_and_find_element(locators.OrderListPageLocators.ORDER_IN_WORK)
        return int(number_in_works.text)

    @allure.step('Проверка открытия окна с деталями заказа')
    def check_open_window_with_order_details(self):
        return self.is_element_present(locators.OrderListPageLocators.INGREDIENT_IN_ORDER)

    @allure.step('Сравнение URL текущей страницы с адресом главной страницы')
    def check_main_page_url(self):
        return self.driver.current_url == urls.BASE_PAGE
