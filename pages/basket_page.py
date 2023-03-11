from selenium.webdriver.common.by import By

from .base_page import BasePage


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(By.CLASS_NAME, "basket-items"), "Basket is not empty"
        assert self.is_element_present(By.XPATH,
                                       "//*[text()[contains(., 'Your basket is empty.')]]"), '"Your basket is empty" text is not present'
