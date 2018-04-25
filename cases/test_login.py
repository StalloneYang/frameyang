#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 12:42
# @Author  : StalloneYang
# @File    : test_login.py
# @desc:
from pages.login.loginPage import LoginPage
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    """登录的测试用例"""
    def setUp(self):
        brower = LoginPage(self)
        self.driver = brower.open_browser(self)
        # self.driver = webdriver.Chrome()
        # self.driver.get("http://dsy.10333.com/")
        self.loginPage = LoginPage(self.driver)


    def tearDown(self):
        self.loginPage.quit_browser()

    def test_login(self):
        """正确的用户名和正确密码登录测试"""
        self.loginPage.click_loginbtn_first()
        self.loginPage.input_username_org("13722222222")
        self.loginPage.input_password_org("88888888")
        self.loginPage.click_loginbtn_org()
        self.loginPage.js_scroll_end()

    def test_login_1(self):
        """正确的用户名和错误密码登录测试"""
        self.loginPage.click_loginbtn_first()
        self.loginPage.input_username_org("13722222222")
        self.loginPage.input_password_org("88888887")
        self.loginPage.click_loginbtn_org()


if __name__ == "__main__":
    unittest.main()




