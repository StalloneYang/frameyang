#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 10:40
# @Author  : StalloneYang
# @File    : test_sendProjectContactFile.py
# @desc: 发送项目联系文件

import unittest
from pages.informationManage.projectContactPage import ProjectContactPage
from pages.login.loginPage import LoginPage


class TestSendProjectContactFile(unittest.TestCase):
    """项目联系文件的测试用例"""
    def setUp(self):
        brower = LoginPage(self)
        self.driver = brower.open_browser(self)
        self.loginPage = LoginPage(self.driver)
        self.projectContactPage = ProjectContactPage(self.driver)

    def tearDown(self):
        self.loginPage.quit_browser()

    def test_sentContact(self):
        """发送项目联系文件"""
        self.loginPage.login_org("sgzb")
        self.projectContactPage.sentFile()
        self.loginPage.click_logoutbtn()

if __name__ == "__main__":
    unittest.main()

