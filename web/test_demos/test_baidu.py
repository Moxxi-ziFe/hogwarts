from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaiduSearch:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://baidu.com/")

    def test_baidu(self):
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹测试学校")
        # self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹测试学校")
        self.driver.find_element(By.CSS_SELECTOR, '[id="kw"]').send_keys("霍格沃兹测试学校")
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
        # self.driver.find_element(By.XPATH, '//div[@id="1"]/h3/a').click()
        # self.driver.find_element(By.CSS_SELECTOR, '[id="1"]>h3>a').click()
        self.driver.find_element(By.CSS_SELECTOR, '#1  > h3 > a').click()
