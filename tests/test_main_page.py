import allure
import data
from conftest import driver
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.user_account_page import UserAccountPage


class TestMainPage:
    @allure.title('Проверка успешного перехода по кнопке "Конструктор"')
    @allure.description('Проверяем успешный клик по кнопке "Конструктор"')
    def test_open_main_page_click_constructor_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        order_list_page = OrderListPage(driver)
        main_page.click_list_order_button()
        order_list_page.click_constructor_button()
        assert order_list_page.check_main_page_url() is True

    @allure.title('Проверка успешного перехода по кнопке "Лента заказов"')
    @allure.description('Проверяем успешный клик по кнопке "Лента заказов"')
    def test_open_list_order_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_list_order_button()
        assert main_page.check_order_list_url() is True

    @allure.title('Проверка открытия окна с данными об ингредиенте')
    @allure.description('Проверяем успешное открытие окна с данными об ингредиенте')
    def test_open_ingredient_card_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient_button()
        assert main_page.check_ingredient_title() is True

    @allure.title('Проверка закрытия окна с данными об ингредиенте')
    @allure.description('Проверяем успешное закрытие окна с данными об ингредиенте')
    def test_close_ingredient_card_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient_button()
        main_page.close_ingredient_card()
        assert main_page.check_main_page_title() is True

    @allure.title('Проверка счетчика ингредиентов')
    @allure.description('Проверяем изменения количества ингредиентов после добавления булочек в конструкторе')
    def test_change_counter_add_constructor_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.add_bun_in_order()
        count_ingredients = main_page.get_count_ingredient()
        assert count_ingredients == '2'

    @allure.title('Проверка успешного оформления заказа авторизованным пользователем')
    @allure.description('Проверяем создание заказа, выполнив авторизацию на сайте')
    def test_authorized_user_create_order_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        # Заходим в личный кабинет
        main_page.click_account_button()
        account_page = UserAccountPage(driver)
        account_page.set_email(data.my_email)
        account_page.set_password(data.my_password)
        account_page.click_enter_button()
        # Создаем заказ
        main_page.find_main_page_title()
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        description_create_order = main_page.find_create_order_description()
        assert description_create_order.text == "Ваш заказ начали готовить"
