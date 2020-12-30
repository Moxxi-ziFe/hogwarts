from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.PageObjectDemo2.Page.Base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def add_member(self, username, account, phone):
        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        # sleep(3)
        check_box = (By.CSS_SELECTOR, '.ww_checkbox')
        # self.wait_until_clickable(check_box)
        # contact_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # contact_name = []
        # for element in contact_list:
        #     contact_name.append(element.get_attribute('title'))
        total_list = []
        while True:
            self.wait_until_clickable(check_box)
            contact_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            contact_name = []
            for element in contact_list:
                contact_name.append(element.get_attribute('title'))
            total_list += contact_name
            if username in contact_name:
                break
            result: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total = result.split('/')
            if num == total:
                break
            else:
                self.find(By.CSS_SELECTOR, '.js_next_page').click()
        return total_list
        # return True

    # def get_member_list(self):
    #     contact_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
    #     contact_name = []
    #     for element in contact_list:
    #         contact_name.append(element.get_attribute('title'))
    #     return contact_name
