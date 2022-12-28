
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_LINK = (By.XPATH, "//span/a[contains(text(),'View basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_TEXT = (By.XPATH, "//*[text()[contains(., 'Your basket is empty.')]]")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:

    # Main page poduct locators
    MAIN_PRODUCT_PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    MAIN_PRODUCT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

    # Alert after adding product to basket locators
    ALERT_PRODUCT_NAME = (By.XPATH, "//*[text()[contains(., 'has been added to your basket')]]")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info.fade.in > div strong")
