"""
Base_page.py 基类模块：主要用于初始化driver， 定义find， 常用的最基本的方法
"""
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
