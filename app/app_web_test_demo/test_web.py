from appium import webdriver


class TestBrowser:
    def setup(self):
        des_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "browserName": "Browser",
            "noReset": "true",
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        pass

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        self.driver.find_element_by_id('index-kw').click()
        self.driver.find_element_by_id('index-kw').send_keys("appium")
        self.driver.find_element_by_id('index-bn').click()
