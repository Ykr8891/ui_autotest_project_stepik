import allure
import pytest
from selenium.webdriver.common.by import By

from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    @allure.title("Guest can go to login page")
    @allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @allure.testcase("http://selenium1py.pythonanywhere.com", 'Test case title')
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    assert page.is_not_element_present(By.CLASS_NAME, "basket-items"), "Basket is not empty"
    assert page.is_element_present(By.XPATH, "//*[text()[contains(., 'Your basket is empty.')]]"), '"Your basket is empty" text is not present'
