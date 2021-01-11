"""
Base_page.py 基类模块：主要用于初始化driver， 定义find， 常用的最基本的方法
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_by_scroll(self, text):
        return self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               f'scrollIntoView(new UiSelector().text("{text}").'
                                                               'instance(0));')

    def get_toast_text(self):
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
