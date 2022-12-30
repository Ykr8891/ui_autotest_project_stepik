import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
    parser.addoption('--headless', action='store', default=False,
                     help="Choose mode")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    if request.config.getoption("headless"):
        options.add_argument("--headless")
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
