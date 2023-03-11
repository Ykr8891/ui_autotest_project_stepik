
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

    def main_product_name_should_equal_alert_product_name(self):
        main_product_name = self.get_main_product_name()
        alert_product_name = self.get_alert_product_name()
        assert main_product_name == alert_product_name, f'Main page name {main_product_name} is nor equal to alert name {alert_product_name}'

    def main_product_price_should_equal_alert_product_price(self):
        main_product_price = self.get_main_product_price()
        alert_product_price = self.get_alert_product_price()
        assert main_product_price == alert_product_price, f'Main page price {main_product_price} is nor equal to alert price {alert_product_price}'

    def success_message_not_presented(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ALERT_PRODUCT_NAME), 'Success message is presented before adding product to basket'

    def success_message_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.ALERT_PRODUCT_NAME), "Success message hasn't disappeared after adding product to basket"
