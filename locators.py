from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_ACCOUNT = (By.XPATH, "(.//a[@class = 'AppHeader_header__link__3D_hX'])[2]")
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    LIST_ORDER_BTN = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_BTN = (By.XPATH, ".//a[@class = '.BurgerIngredient_ingredient__1TVf6'] and text()='Краторная булка N-200i'")
    INGREDIENT_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_LIST = (By.CLASS_NAME, "BurgerIngredients_ingredients__list__2A-mT")
    INGREDIENT_ITEM = (By.CLASS_NAME, "BurgerIngredient_ingredient__1TVf6")
    X_BUTTON = (By.XPATH, "//button[@type='button']")
    BURGER_ORDER = (By.XPATH, "//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")
    BUN_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[2]")
    SAUCE_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[5]")
    MEAT_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[10]")
    CREATE_ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']")
    CREATE_ORDER_DESCRIPTION = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    COUNTER_INGREDIENTS = (By.XPATH, "(//div[contains(@class, '.counter_default__28sqi')])[2]")
    COUNTER = (By.XPATH, "(//p[contains(@class, 'counter_counter__num__3nue1')])[2]")
    CLOSE_WINDOW_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    NUMBER_NEW_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")


class ForgotPassPageLocators:
    RECOVER_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    BUTTON_RECOVERY = (By.XPATH, "//button[text() = 'Восстановить']")
    RECOVER_PASS_TITLE = (By.XPATH, "//h2[text()= 'Восстановление пароля']")
    FIELD_NEW_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']")
    EYE_BUTTON = (By. XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    PASSWORD_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'")
    BUTTON_ACCOUNT = (By.XPATH, "(.//a[@class = 'AppHeader_header__link__3D_hX'])[2]")


class UserAccountLocators:
    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'][1]")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    DESCRIPTION_ACCOUNT = (By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")
    ORDER_HISTORY_BTN = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BTN = (By.XPATH, "//button[text()='Выход']")
    TITLE_LOGIN_PAGE = (By.XPATH, "//h2[text()='Вход']")
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")
    RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")


class OrderListPageLocators:
    ORDER_CARD = (By.XPATH, "(//a[contains(@class,'OrderHistory_link__1iNby')])[2]")
    INGREDIENT_IN_ORDER = (By.XPATH, "(//div[contains(@class,'Modal_imgBox__27yrH')])[1]")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")
    ORDER_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[1]")
    ORDER_COUNTER_TODAY = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[2]")
    NUMBER_READY_ORDER = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default')])[2]")
    ORDER_IN_WORK = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")
