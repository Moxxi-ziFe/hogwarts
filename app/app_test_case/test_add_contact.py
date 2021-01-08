from app.app_page.App import App


class TestAddContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_add_contact(self):
        name = 'hogwarts__007'
        gender = '男'
        phone_number = '12345678907'
        result = self.main.goto_address(). \
            click_add_member(). \
            add_member_menu(). \
            add_contact(name, gender, phone_number). \
            get_toast()
        assert result == '添加成功'
