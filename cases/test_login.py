#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 12:42
# @Author  : StalloneYang
# @File    : test_login.py
# @desc:
import os

import ddt

from pages.login.loginPage import LoginPage
from framework.readExcel import ReadExcel
import unittest
from selenium import webdriver

excel_ = ReadExcel()
gettestdata = excel_.dict_data()

@ddt.ddt
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

    @ddt.data(*gettestdata)
    def test_login(self, d):
        """正确的用户名和正确密码登录测试"""
        self.loginPage.click_loginbtn_first()
        self.loginPage.input_username_org(d['username'])
        self.loginPage.input_password_org(d['password'])
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




