from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.PageObjectDemo.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 扫描二维码
    def scan_qr_code(self):
        pass

    # 进入注册页面
    def goto_register(self):
        self.driver.find_element(By.XPATH, '//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return RegisterPage(self.driver)
