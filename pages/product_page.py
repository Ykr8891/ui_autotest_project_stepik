
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_button.click()

    def get_main_product_name(self):
        return self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_PRODUCT_NAME).text

    def get_main_product_price(self):
        return self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_PRODUCT_PRICE).text

    def get_alert_product_price(self):
        return self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text

    def get_alert_product_name(self):
        alert_product_message = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text

        # Get substring containing just product name
        index = alert_product_message.find(' has been added to your basket.')
        alert_product_name = alert_product_message[0:index]
        return alert_product_name
