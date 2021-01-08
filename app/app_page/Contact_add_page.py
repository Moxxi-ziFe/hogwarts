"""
编辑联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.app_page.Base_page import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_contact(self, name, gender, phone_number):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='姓名　']/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == '男':
            locator = (MobileBy.XPATH, "//*[@text='男']")
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(locator))
            self.driver.find_element(*locator).click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机') and contains(@class, "
                                 "'TextView')]/..//android.widget.EditText").send_keys(
            phone_number)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 局部导入解决循环导入错误
        from app.app_page.Member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
