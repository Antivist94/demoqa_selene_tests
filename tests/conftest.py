import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from utils import attach


@pytest.fixture(scope = "session", autouse = True)
def load_env():
    load_dotenv()

#Todo разобраться с енвами - без них тест работает, также надо дописать шаги со скриншотами и логами
# selenoid_login = os.getenv("SELENOID_LOGIN")
# selenoid_pass = os.getenv("SELENOID_PASS")
# selenoid_url = os.getenv("SELENOID_URL")
selenoid_login = 'user1'
selenoid_pass = '1234'
selenoid_url = 'selenoid.autotests.cloud'


@pytest.fixture(scope = "function", autouse = True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor = f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options = options)

    browser.config.driver = driver

    attach.add_logs(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    yield
    browser.quit()
