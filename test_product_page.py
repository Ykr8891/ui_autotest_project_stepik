import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    main_product_name = page.get_main_product_name()
    main_product_price = page.get_main_product_price()
    page.added_product_name_equals_alert_name(main_product_name)
    page.added_product_price_equals_basket_price(main_product_price)
