import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

SELENIUM_GRID_URL = os.environ.get('SELENIUM_GRID_URL', 'http://127.0.0.1:4444/wd/hub')
os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'
ZULIPRC = 'src/zuliprc'

# Some variables
STAGE_B2C = 'STAGE_URL_GOES_HERE'
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
EMAIL_PRESET = 'SOME@TEST.MAIL'
PASSWORD_PRESET = 'PASSWORD_RESET'
FAKE_MAIL = '@FAKE'


@pytest.fixture(scope="class")
def driver_init_1(request):
    options = ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-application-cache')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-dev-shm-usage")
    web_driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL,
                                  desired_capabilities={"browserName": "chrome", "maxInstances": 2}, options=options)
    web_driver.delete_all_cookies()
    request.cls.driver = web_driver
    yield
    web_driver.quit()


@pytest.fixture(scope="class")
def driver_init_2(request):
    options = FirefoxOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-application-cache')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-dev-shm-usage")
    web_driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL,
                                  desired_capabilities={"browserName": "firefox", "maxInstances": 2}, options=options)
    web_driver.delete_all_cookies()
    request.cls.driver = web_driver
    yield
    web_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter):

    yield

    failure = len(terminalreporter.stats.get('failed', []))
    success = len(terminalreporter.stats.get('passed', []))
    skipped = len(terminalreporter.stats.get('skipped', []))

    f = open('success', 'w')
    f.write(str(success))
    f.close()

    f = open('failure', 'w')
    f.write(str(failure))
    f.close()

    f = open('skipped', 'w')
    f.write(str(skipped))
    f.close()
