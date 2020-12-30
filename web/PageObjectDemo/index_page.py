from selenium import webdriver
from selenium.webdriver.common.by import By

from web.PageObjectDemo.login_page import LoginPage
from web.PageObjectDemo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        # click login
        self.driver.find_element(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # return login page
        return LoginPage(self.driver)

    def goto_register(self):
        # click sign up
        self.driver.find_element(By.XPATH, '//*[@id="tmp"]/div[1]/a').click()
        return RegisterPage(self.driver)
