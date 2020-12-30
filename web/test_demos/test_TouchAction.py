from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(2)

    def test_touch_action(self):
        self.driver.get("https://baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学校")
        action = TouchActions(self.driver)
        action.tap(self.driver.find_element(By.ID, "su")).perform()
        action.scroll_from_element(self.driver.find_element(By.ID, "su"), 0, 10000).perform()
