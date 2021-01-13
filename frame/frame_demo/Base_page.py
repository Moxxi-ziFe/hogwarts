from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        if not driver:
            desire_caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": "true",
                "skipDeviceInitialization": "true",
                "skipServerInitialization": "true",
                "dontStopAppOnReset": "true"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    def find(self, by, locator=None):
        try:
            if not locator:
                return self.driver.find_element(*by)
            return self.driver.find_element(by, locator)
        except Exception as e:
            if self._error_num > self._max_num:
                self._error_num = 0
                raise e
            self._error_num += 1
            for black_ele in self._black_list:
                ele = self.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                return self.find(by, locator)
            raise e