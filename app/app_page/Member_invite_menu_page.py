"""
邀请页面
"""
from appium.webdriver.common.mobileby import MobileBy

from app.app_page.Base_page import BasePage


class MemberInviteMenuPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_member_menu(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 局部导入解决循环导入错误
        from app.app_page.Contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result
