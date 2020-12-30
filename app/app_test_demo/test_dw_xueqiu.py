import pytest
from appium import webdriver
# import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
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

    # def teardown(self):
    #     self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        '''
        1. 打开雪球
        2. 点击搜索输入框
        3. 向搜索输入框输入"阿里巴巴"
        4. 在搜索结果里选择"阿里巴巴"，然后点击
        5. 获取阿里巴巴的股价，并判断这只股价的价格是否 >200
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text
        assert float(current_price) > 200
        # self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]").click()
        # self.driver.back()
        # self.driver.back()

    # Attribute
    def test_attribute(self):
        """
        1. 打开雪球
        2. 点击搜索输入框
        3. 判断搜索框是否可用，并查看搜索框name属性值
        4. 打印搜索框这个元素的左上角坐标和它的宽高
        5. 向搜索输入框输入"alibaba"
        6. 判断"阿里巴巴"是否可见
        7. 如果可见，打印搜索成功，否则打印搜索失败
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(element.text)
        print(element.location)
        print(element.size)
        if element.is_enabled():
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            element_alibaba = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            if element_alibaba.get_attribute("displayed") == 'true':
                print('搜索成功')
            else:
                print('搜索失败')

    # TouchAction
    def test_touch_action(self):
        """
        https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/touch-actions.md
        """
        action = TouchAction(self.driver)
        window_size = self.driver.get_window_rect()
        width = window_size['width']
        height = window_size['height']
        action.press(x=width // 2, y=int(height * 0.8)).wait(200).move_to(x=width // 2,
                                                                          y=int(height * 0.2)).release().perform()

    # XPATH高阶定位
    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_prince = self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert float(current_prince) > 200

    # UiAutomator定位
    def test_my_info(self):
        """
        1. 点击我的，进入个人登录页面
        2. 点击登录，进入登陆页面
        3. 输入用户名，输入密码
        4. 点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    # UiAutomator滚动查找
    def test_scroll_search(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("abcd").'
                                                        'instance(0));').click()

    # 显示等待
    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@text='阿里巴巴']").click()
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/title_container']//*[@text='股票']").click()
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        print(element.text)
        current_price = float(element.text)
        expect_price = 250
        # assert current_price > expect_price
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))

    # Toast
    def test_get_toast(self):
        pass

    # get_attribute
    def test_get_attribute(self):
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(element.get_attribute('resource-id'))
        print(element.get_attribute('content-desc'))

    # 断言
    @pytest.mark.skip
    def test_assert(self):
        a = 10
        b = 20
        assert a < b

    # hamcrest断言
    @pytest.mark.skip
    def test_hamcrest(self):
        assert_that(10, equal_to(10))
        assert_that(10.0, close_to(9.0, 2.0))
        assert_that("strings", contains_string('string'))
