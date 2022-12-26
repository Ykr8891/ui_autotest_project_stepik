
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:

    # Локаторы элементов со страницы продукта
    MAIN_PRODUCT_PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    MAIN_PRODUCT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

    # Локаторы элементов из алертов, возникающих после успешного добавления продукта в корзину
    ALERT_PRODUCT_NAME = (By.XPATH, "//*[text()[contains(., 'has been added to your basket')]]")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info.fade.in > div strong")
