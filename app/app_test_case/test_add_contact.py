from app.app_page.App import App


class TestAddContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_add_contact(self):
        name = 'hogwarts__009'
        gender = '男'
        phone_number = '12345678909'
        result = self.main.goto_address(). \
            click_add_member(). \
            add_member_menu(). \
            add_contact(name, gender, phone_number). \
            get_toast()
        assert result == '添加成功'

    def test_delete(self):
        name = 'baaa4'
        res = self.main.goto_address().goto_edit().search_name(name).delete_member().search_name(name)
        assert not res

    def test_delete_v2(self):
        name = "baaa5"
        res = self.main.goto_address().search_member(name).goto_edit().delete_member().search_member(name)
        assert not res
