import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope = "function", autouse = True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument("--start-maximized")
    browser.config.driver_options = driver_options
    yield
    browser.quit()
