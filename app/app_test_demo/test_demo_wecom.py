from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",
        }
        # "settings[waitForIdleTimeout]": 0
        # "dontStopAppOnReset": "true",
        # "skipDeviceInitialization": 'true',
        # "unicodeKeyBoard": "true",
        # "resetKeyBoard": "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    def test_attendance(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        # settings
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        # sleep(2)
        # print(self.driver.page_source)
        # assert '外出打卡成功' in self.driver.page_source
        WebDriverWait(self.driver, 10).until(lambda x: '外出打卡成功' in x.page_source)
