from appium.webdriver.common.mobileby import MobileBy

from app.app_page.Address_list_page import AddressListPage
from app.app_page.Base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_message(self):
        """
        进入到消息页
        :return:
        """
        pass

    def goto_address(self):
        """
        进入通讯录页面
        :return:
        """
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
