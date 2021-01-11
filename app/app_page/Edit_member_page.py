from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app.app_page.Address_list_page import AddressListPage
from app.app_page.Base_page import BasePage


class EditMemberPage(BasePage):
    def __init__(self, driver, original_page):
        self.driver = driver
        self.original_page = original_page

    def delete_member(self):
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(2)
        if self.original_page == "ManageListPage":
            from app.app_page.Manage_list_page import ManageListPage
            return ManageListPage(self.driver)
        if self.original_page == "PersonalInfoPage":
            return AddressListPage(self.driver)
