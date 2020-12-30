# C:\Program Files (x86)\Google\Chrome\Application\chrome --remote-debugging-port=9222
import shelve
from time import sleep

import pytest
from selenium.webdriver.common.by import By


class TestDemo:
    # @pytest.mark.skip
    def test_demo(self, debugger_driver):
        debugger_driver.get("https://www.baidu.com")

    def test_we_com(self, debugger_driver):
        debugger_driver.switch_to_window(debugger_driver.window_handles[2])
        debugger_driver.find_element(By.ID, 'menu_contacts').click()
        sleep(5)

    # @pytest.mark.skip
    def test_cookie(self, debugger_driver):
        # get_cookies() 获取当前打开页面的cookies
        # add_cookie() 把cookie添加到当前页面
        cookies = debugger_driver.get_cookies()
        # cookies = []
        db = shelve.open("cookies")
        db['WeCom_cookies'] = cookies
        db.close()
        # driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # for cookie in cookies:
        #     driver.add_cookie(cookie)
        # driver.refresh()
        sleep(5)

    def test_shelve(self, driver):
        db = shelve.open("cookies")
        cookies = db['WeCom_cookies']
        db.close()
        driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[1]/a/input').send_keys(
            r'C:\Users\89174\Desktop\Template of batch import to Contacts.xlsx')
        file_name = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[1]/div[2]').text
        assert 'Template of batch import to Contacts.xlsx' == file_name
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/a').click()
        sleep(5)
