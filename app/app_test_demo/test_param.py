import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import close_to
from hamcrest.core import assert_that


class TestParam:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true",
            "dontStopAppOnReset": "true",
            "skipDeviceInitialization": 'true',
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    def teardown(self):
        pass

    @pytest.mark.parametrize('search_key, type, expected_price', [
        ('alibaba', 'BABA', 220),
        ('xiaomi', '01810', 30)
    ])
    def test_param_search(self, search_key, type, expected_price):
        """
        1. 打开雪球应用
        2. 点击 搜索框
        3. 输入 搜索词 'alibaba' or 'xiaomi'
        4. 点击 第一个搜索结果
        5. 判断股票价格
        :return:
        """
        self.driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(search_key)
        # self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name"]').click()
        price = self.driver.find_element_by_xpath(
            f'//*[@text="{type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        self.driver.find_element_by_id('com.xueqiu.android:id/action_close').click()
        price = float(price)
        assert_that(price, close_to(expected_price, expected_price * 0.2))
