# coding:utf8

import pytest
from common.get_driver import get_driver
from pages.login_page import LoginPage
from common.get_testdata import logindatas1,logindatas2

class TestLogin():
    def setup(self):
        self.driver=get_driver()
        self.login=LoginPage(self.driver)
    def teardown(self):
        self.login.driver_quit()

    @pytest.mark.parametrize("dict1",logindatas1)
    def test_login_with_tips(self,dict1):
        self.login.login(username=dict1["username"],password=dict1["password"],check_type=dict1["check_type"])
        content=self.login.get_login_content()
        assert dict1["text"] in content.text

    @pytest.mark.parametrize("dict1",logindatas2)
    def test_login_with_alert(self,dict1):
        self.login.login(username=dict1["username"],password=dict1["password"],check_type=dict1["check_type"])
        alert=self.login.get_alert()
        assert dict1["text"] in alert.text
