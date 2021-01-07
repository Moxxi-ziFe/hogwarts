from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",
            "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "skipServerInitialization": "true"
        }
        # "settings[waitForIdleTimeout]": 0
        # "dontStopAppOnReset": "true",
        # "skipDeviceInitialization": 'true',
        # "unicodeKeyBoard": "true",
        # "resetKeyBoard": "true"
        # 不停止应用直接运行: dontStopAppOnReset, skipDeviceInitialization, skipServerInitialization
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    # def teardown(self):
    #     self.driver.back()

    def test_attendance(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        # settings 动态页面
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        # sleep(2)
        # print(self.driver.page_source)
        # assert '外出打卡成功' in self.driver.page_source
        WebDriverWait(self.driver, 10).until(lambda x: '外出打卡成功' in x.page_source)

    def test_add_member(self):
        name = 'hogwarts__001'
        gender = '男'
        phone_number = '12345678901'
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='姓名　']/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == '男':
            locator = (MobileBy.XPATH, "//*[@text='男']")
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(locator))
            self.driver.find_element(*locator).click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机') and contains(@class, "
                                 "'TextView')]/..//android.widget.EditText").send_keys(
            phone_number)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # sleep(2)
        # print(self.driver.page_source)
        res = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == res
