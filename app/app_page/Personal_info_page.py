from appium.webdriver.common.mobileby import MobileBy

from app.app_page.Base_page import BasePage
from app.app_page.Edit_member_page import EditMemberPage


class PersonalInfoPage(BasePage):
    def goto_edit(self):
        self.find(MobileBy.XPATH, "//*[@text='个人信息']/../../../../../android.widget.LinearLayout[2]").click()
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return EditMemberPage(self.driver, "PersonalInfoPage")
