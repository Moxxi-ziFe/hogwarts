from time import sleep

import pytest

from web.PageObjectDemo2.Page.Main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_add_membber(self):
        username = 'aaaaaaaaaa'
        account = 'aaaaaaaaaa_hogwarts'
        phone = '17800000008'
        add_member = self.main.goto_add_member().add_member(username, account, phone)
        assert username in add_member

    # @pytest.mark.parametrize('username, account, phone', [
    #     ['baaa2', 'baaa2_hogwarts', '17800000122'],
    #     ['baaa3', 'baaa3_hogwarts', '17800000123'],
    #     ['baaa4', 'baaa4_hogwarts', '17800000124'],
    #     ['baaa5', 'baaa5_hogwarts', '17800000125'],
    #     ['baaa6', 'baaa6_hogwarts', '17800000126'],
    # ])
    def test_add_member_from_contact(self):
        username = 'baaa8'
        account = 'baaa8_hogwarts'
        phone = '17800000128'
        add_members = self.main.goto_contacts_page().add_member(username, account, phone)
        print(add_members)
        assert username in add_members
