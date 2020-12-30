from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.PageObjectDemo2.Page.Add_member_page import AddMemberPage
from web.PageObjectDemo2.Page.Base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.implicitly_wait(5)

    def goto_add_member(self):
        # click add member
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        return AddMemberPage(self.driver)

    def goto_contacts_page(self):
        # click contact
        self.find(By.ID, 'menu_contacts').click()
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')

        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, 'username')
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)
        # element = self.wait_until_clickable(locator)
        # element.click()
        return AddMemberPage(self.driver)
