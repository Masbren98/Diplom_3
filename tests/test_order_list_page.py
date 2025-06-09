from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.user_account_page import UserAccountPage
from conftest import driver
import allure
import stellar_burger_api


class TestOrderListPage:
    @allure.title('Проверка успешного открытия окна с "Лента заказов"')
    @allure.description('Проверем успешный клик по кнопке "Лента заказов"')
    def test_open_detail_order_window_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_list_order_button()
        OrderListPage(driver).click_order_card()
        assert OrderListPage(driver).check_open_window_with_order_details()

    @allure.title('Проверка появления номера нового заказа в окне "Лента заказов"')
    @allure.description('Создаём заказ, находим его номер среди всех заказова в окне "Лента заказов"')
    def test_order_in_order_list_success(self, driver):
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
        # Создаём заказ
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        main_page.click_order_card_x_button()
        # Переходим на экран "История заказов" и получаем номер последнего заказа
        main_page.find_main_page_title()
        main_page.click_account_button()
        account_page.click_order_history_btn()
        order_number = account_page.get_order_number()
        # Переходим на экран "Лента заказов" и получаем номер последнего заказа
        main_page.click_list_order_button()
        order_list_page = OrderListPage(driver)
        order_number_in_list = order_list_page.get_order_number()
        assert order_number == order_number_in_list

    @allure.title('Проверка увеличения значения счётчика заказов в окне "Лента заказов"')
    @allure.description('Создаём заказ и проверяем что счётчик всех заказов в окне "Лента заказов" увеличивается на 1')
    def test_order_counter_increases_when_new_order_is_placed_success(self, driver):
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
        # Получаем значение счётчика заказов на странице "Лента заказов"
        main_page.click_list_order_button()
        order_list_page = OrderListPage(driver)
        counter_before = order_list_page.get_orders_counter()
        # Создаём новый заказ
        order_list_page.click_constructor_button()
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        main_page.click_order_card_x_button()
        # Переходим на экран "Лента заказов" и получаем значение счётчика всех заказов
        main_page.click_list_order_button()
        counter_after = order_list_page.get_orders_counter()
        assert (counter_after - counter_before) == 1

    @allure.title('Проверка увеличения значения счётчика "Выполнено за сегодня" в окне "Лента заказов"')
    @allure.description('Создаём заказ и проверяем что счётчик выполненных заказов за сегодня, в окне "Лента заказов", увеличивается на 1')
    def test_order_counter_today_increases_when_new_order_is_placed_success(self, driver):
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
        # Получаем значение счётчика выполненных за сегодня заказов на странице "Лента заказов"
        main_page.click_list_order_button()
        order_list_page = OrderListPage(driver)
        counter_before = order_list_page.get_orders_counter_today()
        # Создаем новый заказ
        order_list_page.click_constructor_button()
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        main_page.click_order_card_x_button()
        # Переходим на экран "Лента заказов" и получаем значение счётчика выполненных за сегодня заказов
        main_page.click_list_order_button()
        counter_after = order_list_page.get_orders_counter_today()
        assert (counter_after - counter_before) == 1

    @allure.title('Проверка появления номера нового заказа в окне "Лента заказов" в разделе "В работе"')
    @allure.description('Создаём заказ, находим его номер в окне "Лента заказов" в разделе "В работе"')
    def test_number_appears_in_progress_section_success(self, driver):
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
        # Создаем новый заказ, получаем его номер
        main_page.add_bun_in_order()
        main_page.add_sauce_in_order()
        main_page.add_meat_in_order()
        main_page.click_create_order_button()
        new_order_number = main_page.get_new_order_number()
        main_page.click_order_card_x_button()
        # Переходим на экран "Лента заказов" и получаем номер заказа, попавшего столбец "В работе"
        main_page.click_list_order_button()
        order_list_page = OrderListPage(driver)
        number_in_order_list = order_list_page.get_order_in_works_number()
        assert number_in_order_list == new_order_number
