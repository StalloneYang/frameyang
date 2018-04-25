#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 10:23
# @Author  : StalloneYang
# @File    : projectContactPage.py
# @desc:项目联系文件

from framework.base import BasePage
from framework.getconfig import GetConfig
from framework.logger import Logger

logger = Logger(logger="ProjectContactPage").getlog()
getconfig = GetConfig()

class ProjectContactPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.info_manage = "xpath=>//span[contains(.,'信息管理')]"  # 横条导航 信息管理
        self.project_contact = "xpath=>//span[contains(.,'项目联系文件')]"  # 信息管理菜单下拉的“项目联系文件”
        self.new_file = "xpath=>//span[@data-reactid='.0.$0/=10.3.$0/=10.0.1.0.1.0.0.0']"  # 新建按钮
        self.first_file = "xpath=>//input[@data-reactid='.1.1.0.1.0.3:$0.0.0']"  # 选择第一个工程联系文件
        self.confirm_select_file = "xpath=>//button[contains(.,'确定')]"  # 选择文件后的确认按钮
        self.submitBtn = "xpath=>//button[contains(.,'提交')]"  # 提交按钮

    def move_to_info_manage(self):
        """横条导航 信息管理"""
        self.move_to_element(self.info_manage)

    def click_project_contact(self):
        """信息管理菜单下拉的“项目联系文件”"""
        self.click(self.project_contact)

    def click_new_file(self):
        """新建按钮"""
        self.click(self.new_file)

    def click_first_file(self):
        """选择第一个工程联系文件"""
        self.click(self.first_file)

    def click_confirm_select_file(self):
        """选择文件后的确认按钮"""
        self.click(self.confirm_select_file)

    def click_submitBtn(self):
        """提交按钮"""
        self.click(self.submitBtn)

    def sentFile(self):
        """发送文件的流程"""
        self.move_to_info_manage()
        self.click_project_contact()
        self.click_new_file()
        self.click_first_file()
        self.click_confirm_select_file()
        self.switch_window()
        self.click_submitBtn()
