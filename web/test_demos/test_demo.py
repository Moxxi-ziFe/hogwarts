from selenium import webdriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    # def teardown(self):
    # self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("https://ceshiren.com/")
        # sleep(1)
        self.driver.find_element_by_link_text("开源项目").click()
        # sleep(1)
        self.driver.find_element_by_link_text("定制pytest插件必备之pytest hook的执行顺序").click()

        # sleep(3)
        # self.driver.find_element_by_css_selector(".badge-wrapper:nth-child(2) .category-name").click()
        def wait(x):
            return len(self.driver.find_element_by_css_selector(".badge-wrapper:nth-child(2) .category-name")) >= 1

        # WebDriverWait(self.driver, 10).until(expected_conditions.)
        self.driver.find_element_by_css_selector(".badge-wrapper:nth-child(2) .category-name").click()
