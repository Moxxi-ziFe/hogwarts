import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.maximize_window()
    return driver


@pytest.fixture()
def debugger_driver():
    option = Options()
    option.debugger_address = "127.0.0.1:9222"
    debugger_driver = webdriver.Chrome(options=option)
    debugger_driver.implicitly_wait(2)
    return debugger_driver
