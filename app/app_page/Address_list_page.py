# 通讯录界面
from appium.webdriver.common.mobileby import MobileBy

from app.app_page.Base_page import BasePage
from app.app_page.Member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_add_member(self):
        self.find_by_scroll('添加成员').click()
        return MemberInviteMenuPage(self.driver)

    def goto_edit(self):
        self.find(MobileBy.XPATH,
                  "//*[@text='ziFe']/../../../../.."
                  "/android.widget.LinearLayout[2]"
                  "/android.widget.RelativeLayout[2]"
                  "/android.widget.TextView").click()
        from app.app_page.Manage_list_page import ManageListPage
        return ManageListPage(self.driver)

    def search_member(self, name):
        try:
            self.find_by_scroll(name).click()
            from app.app_page.Personal_info_page import PersonalInfoPage
            return PersonalInfoPage(self.driver)
        except:
            return False
