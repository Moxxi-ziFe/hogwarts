from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestJS:
    # @pytest.mark.skip
    def test_js_scroll(self, driver):
        driver.get("https://baidu.com/")
        driver.find_element(By.ID, 'kw').send_keys('selenium测试')
        element = driver.execute_script("return document.getElementById('su')")
        element.click()
        driver.execute_script("document.documentElement.scrollTop = 10000")
        driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]').click()
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(driver.execute_script(code))
        sleep(5)

    def test_datetime(self, driver):
        driver.get("https://www.12306.cn/index/")
        # driver.execute_script('a=document.getElementById("train_date"); a.removeAttribute("readonly")')
        # driver.execute_script('document.getElementById("train_date").value="2020-12-30"')
        element_from = driver.find_element(By.XPATH, '//*[@id="fromStationText"]')
        element_to = driver.find_element(By.ID, 'toStationText')

        action = ActionChains(driver)
        # action.move_to_element(element_from)
        action.click(element_from).pause(1)
        action.send_keys('北京').pause(1)
        action.send_keys(Keys.ENTER).pause(1)
        action.click(element_to).pause(1)
        action.send_keys('济南').pause(1)
        action.send_keys(Keys.ENTER).pause(1)
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="fromStationText"]')))
        action.perform()

        # element_from.click()
        # element_from.send_keys('北京')
        # element_from.send_keys(Keys.ENTER)
        # element_to.click()
        # element_to.send_keys('南京')
        # element_to.send_keys(Keys.ENTER)

        driver.execute_script('a=document.getElementById("train_date"); a.removeAttribute("readonly")')
        driver.execute_script('document.getElementById("train_date").value="2020-12-30"')

        driver.find_element(By.ID, 'search_one').click()
        sleep(5)
        # print(driver.execute_script('return document.getElementById("train_date").value'))
