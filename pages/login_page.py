import allure

from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):

    @allure.step('Check if current page is login page')
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step('Check if current url is login page url')
    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url

    @allure.step('Check if login form is presented')
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    @allure.step('Check if register form is presented')
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_register_form()
        self.fill_email_field(email)
        self.fill_password_fields(password)
        self.submit_registration()

    def go_to_login_register_form(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def fill_email_field(self, email):
        field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        field.send_keys(email)

    def fill_password_fields(self, password):
        field1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        field2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        field1.send_keys(password)
        field2.send_keys(password)

    def submit_registration(self):
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        button.click()
