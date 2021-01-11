from app.app_page.Base_page import BasePage


class ManageListPage(BasePage):
    def search_name(self, name):
        try:
            self.find_by_scroll(name).click()
            from app.app_page.Edit_member_page import EditMemberPage
            return EditMemberPage(self.driver, 'ManageListPage')
        except:
            return False
