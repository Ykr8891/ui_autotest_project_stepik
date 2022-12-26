
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket button is not presented " \
                                                                                 "on product description section"
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_button.click()

    def get_main_product_name(self):
        assert self.is_element_present(*ProductPageLocators.MAIN_PRODUCT_PRODUCT_NAME), "Product name element is not presented " \
                                                                                        "on product description section"
        return self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_PRODUCT_NAME).text

    def get_main_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MAIN_PRODUCT_PRODUCT_PRICE), "Product price element is not presented " \
                                                                                         "on product description section"
        return self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_PRODUCT_PRICE).text

    def added_product_price_equals_basket_price(self, product_price):
        """

        """
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_PRICE), "Alert product price element is not presented " \
                                                                                  "in alert section"
        alert_product_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert product_price == alert_product_price, f'Main page price {product_price} is nor equal to alert price {alert_product_price}'

    def added_product_name_equals_alert_name(self, product_name):
        """

        """
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), "Alert product name element is not presented " \
                                                                                 "in alert section"
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert product_name in alert_product_name, f'Main page name {product_name} is nor equal to alert name {alert_product_name}'
