import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    # def teardown(self):
    # self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, "/html/body/form/input[3]")
        element_double_click = self.driver.find_element(By.XPATH, "/html/body/form/input[2]")
        element_right_click = self.driver.find_element(By.CSS_SELECTOR,
                                                       "body > form > input[type=button]:nth-child(13)")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_right_click)
        action.double_click(element_double_click)
        action.perform()

    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        element_drag = self.driver.find_element(By.ID, "dragger")
        element_drop = self.driver.find_element(By.XPATH, '/html/body/div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(element_drag, element_drop)
        # action.click_and_hold(element_drag).release(element_drop)
        action.click_and_hold(element_drag).move_to_element(element_drop).release()
        action.perform()

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        element = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        action = ActionChains(self.driver)
        action.click(element)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
